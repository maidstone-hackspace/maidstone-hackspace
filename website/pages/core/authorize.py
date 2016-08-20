import os
import uuid
import hashlib
import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, flash
from flask import redirect, abort
from flask import make_response
from flask import request
from flask import Blueprint
from flask.ext.login import current_user, LoginManager, login_required, UserMixin, login_user, logout_user, make_secure_token
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix

from scaffold import web
from libs.mail import sendmail
from pages import header, footer
from data import site_user
from config.settings import *
from constants import *

web.load_widgets('widgets')

authorize_pages = Blueprint('authorize_pages', __name__, template_folder='templates')

login_manager = LoginManager()
login_manager.login_view = '/login'

oauth_lookup_id = {'google':1, 'github':2, 'facebook':3}
oauth_lookup_name = dict((v, k) for k, v in oauth_lookup_id.items())


def is_weak_password(password1, password2):
    if password1 != password2:
        password1 = password2 = None
        return True

    # TODO check length and chars
    password1 = password2 = None
    return False
    

#~ def todict(data):
    #~ new_dict = {}
    #~ for key, value in data.items():
        #~ new_dict[key] = value
    #~ return new_dict


class User(UserMixin):
    def __init__(self, user_id, active=True):
        self.id = None
        user_details = site_user.get_user_details({'id': user_id}).get()
        self.active = False
        if user_details:
            self.active = True
            #~ self.check_password(user_details.get('password'))
            self.id = user_id
            self.name = user_details.get('username')
            #~ self.is_authenticated = self.active

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
    """Flask user loader hook, internal to flask login"""
    return User(userid)


@login_manager.token_loader
def load_token(request):
    token = request.headers.get('Authorization')
    if token is None:
        token = request.args.get('token')
     
    if token is not None:
        username, password = token.split(":")  # naive token
        user_entry = User.get(username)
    if (user_entry is not None):
        user = User(user_entry[0], user_entry[1])
        
    if (user.password == password):
        return user
    return None 

#~ def auth_required():
    #~ if not session.get('user_id'):
        #~ redirect(domain + '/login', 301)

@authorize_pages.route("/register", methods=['GET'])
def register_form():
    header('Register for access')
    web.page.create('Register for access')
    #~ web.page.section(web.register_form.create().render())

    web.form.create('Register new user account', '/register')
    web.form.append(name='name', label='Your full name', placeholder='Ralf Green', value='')
    web.form.append(name='email', label='Valid Email', placeholder='ralf@maidstone-hackspace.org.uk', value='')
    web.form.append(input_type='password', name='password', label='Password', placeholder='quick brown fox jumped over', value='')
    web.form.append(input_type='password', name='password_confirm', label='Password Confirm', placeholder='quick brown fox jumped over', value='')

    web.page.section(web.form.render())
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
        redirect('/register')

    header('Your account has been registered')
    web.page.create('Your account has been registered')

    new_user = site_user.create()
    new_user.execute(data)
    flash('Your account has now been created')
    
    web.template.body.append(web.page.set_classes('page col s10 offset-s1').render())
    return make_response(footer())

@authorize_pages.route("/oauth/<provider>/<start_oauth_login>/", methods=['GET'])
@authorize_pages.route("/oauth/<provider>/<start_oauth_login>", methods=['GET'])
@authorize_pages.route("/oauth/<provider>/", methods=['GET'])
@authorize_pages.route("/oauth/<provider>", methods=['GET'])
def oauth(provider, start_oauth_login=False):
    oauth_verify = True
    oauth_provider = oauth_conf.get(provider)
    oauth_access_type = ''
    oauth_approval_prompt = ''
    if oauth_live is False:
        print('offline testing')
        oauth_verify = False
        oauth_access_type = 'offline'
        oauth_approval_prompt = "force"
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    if start_oauth_login:
        oauth_session = OAuth2Session(
            oauth_provider.get('client_id'), 
            scope=oauth_provider.get('scope'), 
            redirect_uri=request.url_root + oauth_provider.get('redirect_uri'))

        if provider == 'facebook':
            oauth_session = facebook_compliance_fix(oauth_session)

        authorization_url, state = oauth_session.authorization_url(
            oauth_provider.get('auth_uri'),
            access_type=oauth_access_type,
            approval_prompt=oauth_approval_prompt)

        # State is used to prevent CSRF, keep this for later, make sure oauth returns to the same url.
        # if testing and oauth_state errors make sure you logged in with localhost and not 127.0.0.1
        session['oauth_state'] = state
        session.modified = True
        return redirect(authorization_url)

    if session.get('oauth_state', None) is None:
        flash('Something went wrong, oauth session not started')
        return redirect('/login')
    
    # allready authorised so lets handle the callback
    oauth_session = OAuth2Session(
        oauth_provider.get('client_id'), 
        state=session['oauth_state'], 
        redirect_uri=request.url_root + oauth_provider.get('redirect_uri'))

    if provider == 'facebook':
        oauth_session = facebook_compliance_fix(oauth_session)
    

    # code error is todo with authorisation response
    oauth_session.fetch_token(
        oauth_provider.get('token_uri'),
        client_secret=oauth_provider.get('client_secret'),
        authorization_response=request.url,
        verify=oauth_verify)

    # Fetch a protected resource, i.e. user profile
    response = oauth_session.get(oauth_provider.get('user_uri'))
    oauth_response = response.json()
    
    oauth_id = oauth_response.get('login') or oauth_response.get('id')
    provider_id = oauth_lookup_id.get(provider)
    oauth_user = site_user.fetch_oauth_login({
        'username': oauth_id or '',
        'provider': provider_id
    }).get()

    if oauth_user: 
        user_details = site_user.get_user_details({
            'id': oauth_user.get('user_id')
        }).get()

        # we have matched a user so login and redirect
        if user_details:
            login_user(User(user_details.get('user_id')))
            # no E-Mail so lets ask the user to set there email before allowing login
            if not user_details.get('email'):
                return redirect('/profile/change_email')
            return redirect('/profile')

    flash('Your new profile has been created, and your now logged in')

    if current_user.get_id():
        # link oauth to users account
        site_user.create_oauth_login().execute({
            'user_id': current_user.get_id(), 
            'username': oauth_id or '', 
            'provider': provider_id})
        return redirect('/profile')

    # create new user from oauth information

    new_user_details = {
        'password': 'oauth', 
        'profile_image': oauth_response.get('picture'),
        'username': oauth_id,
        'first_name': oauth_response.get('given_name') or '',
        'last_name': oauth_response.get('family_name') or ''}

    if  oauth_response.get('email'):
        new_user_details['email']= oauth_response.get('email')

    user_id = site_user.create().execute(new_user_details)

    # register oauth login creation
    site_user.create_oauth_login().execute({
        'user_id': user_id, 
        'username': oauth_id or '', 
        'provider': provider_id})

    login_user(User(user_id))
    site_user.update_last_login().execute({'id': user_id})
    if not user_id:
        flash('Failed to create user')
        return redirect('/login')
    return redirect('/profile')


@authorize_pages.route("/change-password/<code>", methods=['GET'])
@authorize_pages.route("/change-password", methods=['GET'])
def change_password(code=None):
    #if we have a code this is a password reset, so try and login the user first
    site_user.delete_password_reset().execute({})
    if code:
        
        user_details = site_user.get_user_by_reset_code({'reset_code': code}).get()

        if not user_details:
            #invalid code so pretend the page does not even exist
            return abort(404)
        #check the code has not expired
        #datetime.datetime.now() + datetime.timedelta(minutes=15)
        has_date_expired = user_details.get('created') + datetime.timedelta(minutes=60)
        if has_date_expired < datetime.datetime.now():
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
    web.template.body.append(web.page.set_classes('page col s10 offset-s1').render())
    return make_response(footer())

@login_required
@authorize_pages.route("/change-password", methods=['POST'])
def change_password_submit(code=None):
    if not session.get('user_id'):
        abort(404)

    if is_weak_password(request.form.get('password'), request.form.get('password_confirm')):
        redirect('/login')

    pw_hash = generate_password_hash(request.form.get('password'))
    user_details = site_user.authorize({
        'id': session.get('user_id')}).get()
    site_user.change_password().execute({
        'id': user_details.get('user_id'), 
        'password': pw_hash})
    
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
        sendmail().send(
            from_address='no-reply@maidstone-hackspace.org.uk', 
            to_address='oly@leela', 
            subject="Reset password request", 
            body=body)
    
    # display success page, dont give away anything about if the email is actually registered
    web.template.create('Maidstone Hackspace - Password reset')
    header('Password reset')
    web.page.create('Password reset sent')
    web.page.section(
        web.paragraph.create('If this E-Mail is registered you will shortly be reciving an E-Mail with reset details').render()
    )
    web.template.body.append(web.page.render())
    return make_response(footer())

@authorize_pages.route("/login/failure", methods=['GET'])
def login_Failure():
    web.template.create('%s - Login' % site_name)
    header('Login Failure')
    web.page.create('Login Failure')
    #~ web.template.body.append(web.messages.render())
    web.template.body.append(web.page.render())
    return make_response(footer())


@authorize_pages.route("/logout")
def logout():
    logout_user()
    return redirect('/')
