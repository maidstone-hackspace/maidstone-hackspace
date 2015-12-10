import os
import sys
import time
import uuid
import hashlib
import datetime

from werkzeug import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, session, flash, get_flashed_messages
from flask import redirect, abort
from flask import make_response
from flask import request
from flask import Blueprint
from flask.ext.login import LoginManager, login_required, UserMixin, login_user, logout_user, current_user, make_secure_token
from requests_oauthlib import OAuth2Session


from scaffold import web
from libs.mail import sendmail
from pages import header, footer
from pages import profile
from data import site_user
from config.settings import *
from constants import *

web.load_widgets('widgets')

authorize_pages = Blueprint('authorize_pages', __name__, template_folder='templates')

login_manager = LoginManager()
login_manager.login_view = '/login'


def is_weak_password(password1, password2):
    if password1 != password2:
        password1 = password2 = None
        return True

    # TODO check length and chars
    
    password1 = password2 = None
    return False
    

def todict(data):
    new_dict = {}
    for key, value in data.items():
        new_dict[key] = value
    return new_dict


class User(UserMixin):
    def __init__(self, user_id, active=True):
        print 'logged in ###########'
        print user_id
        user_details = site_user.get_user_details({'id': user_id}).get()
        self.active = False
        print user_details
        if user_details:
            #~ self.check_password(user_details.get('password'))
            self.id = user_id
            self.name = user_details.get('username')
            self.team_id = user_details.get('team_id', 1)
            self.active = active

    def get_id(self):
        return self.id

    def is_active(self):
        return self.active

    def is_authenticated(self):
        return self.active
        
    def get_auth_token(self):
        return make_secure_token(self.name, key='deterministic')


@login_manager.user_loader
def load_user(userid):
    return User(userid)


@login_manager.token_loader
def load_token(request):
    token = request.headers.get('Authorization')
    if token is None:
        token = request.args.get('token')
     
    if token is not None:
        username, password = token.split(":")  # naive token
        print username
        print password
        user_entry = User.get(username)
    if (user_entry is not None):
        user = User(user_entry[0], user_entry[1])
        
    if (user.password == password):
        return user
    return None 

def auth_required():
    if not session.get('user_id'):
        redirect(domain + '/login', 301)

@authorize_pages.route("/register", methods=['GET'])
def register_form():
    header('Register for access')
    web.page.create('Register for access')
    web.page.section(web.register_form.create().render())
    web.template.body.append(web.page.render())
    return make_response(footer())

@authorize_pages.route("/register", methods=['POST'])
def register_submit():
    data = {}
    data['email'] = request.form.get('email')
    data['username'] = request.form.get('email')
    data['first_name'] = request.form.get('name').strip().split()[0]
    data['last_name'] = request.form.get('name').strip().split()[-1]
    
    data['password'] = request.form.get('password')
    data['password_confirm'] = request.form.get('password')
    
    
    data['password'] = generate_password_hash(request.form.get('password'))
    #TODO password strength tests
    if is_weak_password(request.form.get('password'), request.form.get('password_confirm')):
        print 'password not strong enough'
        redirect('/register')

    header('Your account has been registered')
    web.page.create('Your account has been registered')

    new_user = site_user.create()
    new_user.execute(data)
    flash('Your account has now been created')
    
    web.template.body.append(web.page.render())
    return make_response(footer())

@authorize_pages.route("/oauth", methods=['GET'])
@authorize_pages.route("/oauth/", methods=['GET'])
@authorize_pages.route("/oauth/<provider>", methods=['GET'])
def oauth(provider=None):
    oauth_verify = True
    oauth_provider = oauth_conf.get('google')
    oauth_access_type = ''
    oauth_approval_prompt = ''
    if oauth_live is False:
        oauth_verify = False
        oauth_access_type = 'offline'
        oauth_approval_prompt = "force"
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    print session
    if provider:
        oauth_session = OAuth2Session(
            oauth_provider.get('client_id'), 
            scope=oauth_provider.get('scope'), 
            redirect_uri=oauth_provider.get('redirect_uri'))

        # offline for refresh token
        # force to always make user click authorize
        #generate the google url we will use to authorize and redirect there
        authorization_url, state = oauth_session.authorization_url(
            oauth_provider.get('auth_uri'),
            access_type=oauth_access_type,
            approval_prompt=oauth_approval_prompt)

        # State is used to prevent CSRF, keep this for later, make sure oauth returns to the same url.
        session['oauth_state'] = state
        return redirect(authorization_url)

    print session
    #allready authorised so lets handle the callback
    oauth_session = OAuth2Session(
        oauth_provider.get('client_id'), 
        state=session['oauth_state'], 
        redirect_uri=oauth_provider.get('redirect_uri'))

    token = oauth_session.fetch_token(
        oauth_provider.get('token_uri'),
        client_secret=oauth_provider.get('client_secret'),
        authorization_response=request.url,
        verify=oauth_verify)

    # Fetch a protected resource, i.e. user profile
    r = oauth_session.get('https://www.googleapis.com/oauth2/v1/userinfo')

    oauth_user = r.json()

    #https://www.googleapis.com/auth/plus.login
    #https://www.googleapis.com/auth/plus.me

    print oauth_user
    user_details = site_user.get_by_email({
        'email': oauth_user.get('email')
    }).get()    

    if not user_details:
        flash('Your new profile has been created, and your now logged in')
        site_user.create().execute({
            'email': oauth_user.get('email'), 
            'password': 'oauth', 
            'profile_image': oauth_user.get('picture'),
            'username': oauth_user.get('email'),
            'first_name': oauth_user.get('given_name'),
            'last_name': oauth_user.get('family_name')})
        user_details = site_user.get_by_email({
            'email': oauth_user.get('email')
        }).get()
    
    user = User(user_details.get('user_id'))
    login_user(user)
    site_user.update_last_login().execute(user_details)
    return redirect('/profile')

@authorize_pages.route("/change-password/<code>", methods=['GET'])
@authorize_pages.route("/change-password", methods=['GET'])
def change_password(code=None):
    #if we have a code this is a password reset, so try and login the user first
    print code
    site_user.delete_password_reset().execute({})
    if code:
        
        user_details = site_user.get_user_by_reset_code({'reset_code': code}).get()

        print user_details
        if not user_details:
            #invalid code so pretend the page does not even exist
            return abort(404)
        #check the code has not expired
        #datetime.datetime.now() + datetime.timedelta(minutes=15)
        has_date_expired = user_details.get('created') + datetime.timedelta(minutes=60)
        if has_date_expired < datetime.datetime.now():
            print 'date expired'
            #date expired so clean up and pretend the page does not exist
            return abort(404)
        #challenge passed so login the user so they can change there password
        login_user(
            User(user_details.get('user_id'))
        )
        session['user_id'] = str(user_details.get('user_id'))
        
    web.template.create('Maidstone Hackspace - Profile')
    header('User profile')
    web.page.create('Change password')
    web.page.section(
        web.change_password_box.create().render()
    )
    web.template.body.append(web.page.render())
    return make_response(footer())

@login_required
@authorize_pages.route("/change-password", methods=['POST'])
def change_password_submit(code=None):
    if not session.get('user_id'):
        abort(404)
    user_details = site_user.authorize({
        'id': session.get('user_id')}).get()

    if is_weak_password(request.form.get('password'), request.form.get('password_confirm')):
        print 'password not strong enough'
        redirect('/login')
    
    pw_hash = generate_password_hash(request.form.get('password'))
    
    site_user.change_password().execute({'id': user_details.get('user_id'), 'password': pw_hash})
    
    web.template.create('Maidstone Hackspace - Profile')
    header('User Profile')
    web.page.create('Password change complete')
    web.page.section(
        'Your password has successfull been changed'
    )
    web.template.body.append(web.page.render())
    return make_response(footer())



@authorize_pages.route("/reset-password", methods=['GET'])
def reset_password():
    web.template.create('Maidstone Hackspace - Login')
    header('Members Login')
    web.page.create('Forgot password reset')
    web.page.section(
        web.password_box.create('Please enter your E-Mail account', reset=True).render()
    )
    web.template.body.append(web.page.render())
    return make_response(footer())

@authorize_pages.route("/reset-password", methods=['POST'])
def reset_password_submit():
    user_details = site_user.get_by_username({
        'email': request.form.get('email')}).get()
    
    reset_code = hashlib.sha256(str(uuid.uuid4())).hexdigest()
    
    if user_details:
        site_user.create_password_reset()   \
                 .on_duplicate()            \
                 .execute({
                    'user_id': str(user_details.get('user_id')), 
                    'reset_code': reset_code})
        
        l=web.link.create(title='Change password', content='Click to change password',link="{domain}change-password/{resetcode}".format(**{'domain':app_domain, 'resetcode': reset_code})).render()
        
        body = "Please follow the link below to change your password.\n" + l
        body += "{domain}change-password/{resetcode}".format(**{'domain':app_domain, 'resetcode': reset_code})
        sendmail().send(from_address='no-reply@maidstone-hackspace.org.uk', to_address='oly@leela', subject="Reset password request", body=body)
    
    # display success page, dont give away anything about if the email is actually registered
    web.template.create('Maidstone Hackspace - Password reset')
    header('Password reset')
    web.page.create('Password reset sent')
    web.page.section(
        web.paragraph.create('If this E-Mail is registered you will shortly be reciving an E-Mail with reset details').render()
    )
    web.template.body.append(web.page.render())
    return make_response(footer())


@authorize_pages.route("/login", methods=['GET'])
def login_screen():
    web.template.create('Maidstone Hackspace - Login')
    header('Members Login')
    web.page.create('Member Login')
    web.page.section(
        web.login_box.create().enable_oauth('google').render()
    )
    #~ web.template.body.append(web.messages.render())
    web.template.body.append(web.page.render())
    return make_response(footer())


@authorize_pages.route("/login", methods=['POST'])
def login_screen_submit():
    """handle the login form submit"""
    # try to find user by username
    user_details = site_user.get_by_username({
        'email': request.form.get('username')}).get()

    #not found so lets bail to the login screen
    if not user_details:
        flash('Failed to login with that username and password, please retry.')
        return login_screen()

    #now lets verify the users password, and bail if its wrong
    pw_hash = generate_password_hash(request.form.get('password'))
    if check_password_hash(pw_hash, user_details.get('password')):
        flash('Failed to login with that username and password, please retry.')
        return login_screen()

    #login user and redirect to profile
    login_user(
        User(user_details.get('user_id'))
    )
    flash('You have successfully logged in !')
    #~ session['username'] = user_details.get('username', 'anonymous')
    #~ session['user_id'] = str(user_details.get('user_id'))
    site_user.update_last_login(user_details)
    return redirect('/profile')


@authorize_pages.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')
