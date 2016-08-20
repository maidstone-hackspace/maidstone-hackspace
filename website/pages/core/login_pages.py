import os

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
from pages.core.authorize import User
from data import site_user
from config.settings import *
from constants import *


login_pages = Blueprint('login_pages', __name__, template_folder='templates')


@login_pages.route("/login", methods=['GET'])
def login_screen():
    web.template.create('Maidstone Hackspace - Login')
    header('Members Login')
    web.page.create('Member Login')
    web.page.section(
        web.loginBox.create().enable_oauth('google').enable_oauth('facebook').enable_oauth('github').render()
    )
    web.template.body.append(web.page.set_classes('page col s10 offset-s1').render())
    return make_response(footer())


@login_pages.route("/login", methods=['POST'])
def login_screen_submit():
    """handle the login form submit"""
    # try to find user by username
    user_details = site_user.get_by_username({
        'username': request.form.get('username')}).get()

    # not found so lets bail to the login screen
    if not user_details:
        flash('Failed to login with that username and password, please retry.')
        return redirect('/login')

    # now lets verify the users password, and bail if its wrong
    pw_hash = generate_password_hash(request.form.get('password'))
    if check_password_hash(pw_hash, user_details.get('password')):
        flash('Failed to login with that username and password, please retry.')
        return redirect('/login')

    #login user and redirect to profile
    login_user(
        User(user_details.get('user_id'))
    )

    flash('You have successfully logged in !')
    site_user.update_last_login().execute({'id': user_details.get('user_id')})

    # logged in but no E-Mail so lets ask the user for there email.
    if not user_details.get('email'):
        return redirect('/profile/change_email')

    return redirect('/profile')


@login_pages.route("/profile/change_email", methods=['GET'])
@login_required
def change_email_get():
    web.template.create('%s - Change Email' % site_name)
    header('Members Login')
    web.page.create('Set your E-Mail address')
    
    web.form.create('Set E-Mail address for account', '/profile/change_email')
    web.form.append(name='email', label='Valid Email', placeholder='ralf@maidstone-hackspace.org.uk', value='')
    
    web.page.section(web.form.render())
    web.template.body.append(web.page.render())
    return make_response(footer())

@login_pages.route("/profile/change_email", methods=['POST'])
@login_required
def change_email_post():
    flash('An E-Mail has been sent to you please check and confirm you identity.')
    sendmail().send(
        from_address='no-reply@maidstone-hackspace.org.uk', 
        to_address='oly@leela', 
        subject="%s - Confirm E-Mail Address" % site_name, 
        body='generate link here')

    site_user.update_user_email().execute({
        'id': current_user.get_id(), 
        'email': request.form.get('email')
    })
    return redirect('/profile')
