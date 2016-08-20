import os
import sys
from flask import Flask, send_from_directory
from flask import make_response

sys.path.append(os.path.abspath('../../../scaffold/'))
sys.path.insert(0,os.path.abspath('../../../scaffold/'))

from config import settings
import generate
from pages import homepage
from pages import chat
from pages import blog
from pages import members
from pages.contact import contact_page, submit_contact_page

from pages.core.login_pages import login_pages
from pages.core.authorize import authorize_pages, login_manager
from pages.donate import donate_pages
from pages.google_groups import google_groups_pages
from pages.equipment import equipment_pages
from pages.profile import profile_pages


web_app = Flask(__name__, static_folder='static')
web_app.config['PROPAGATE_EXCEPTIONS'] = True
web_app.secret_key = settings.flask_secret_key
login_manager.init_app(web_app)

web_app.register_blueprint(login_pages)
web_app.register_blueprint(authorize_pages)
web_app.register_blueprint(equipment_pages)
web_app.register_blueprint(profile_pages)
web_app.register_blueprint(google_groups_pages)
web_app.register_blueprint(donate_pages)

#~ @web_app.route('/static/<path:filename>')
#~ def send_js(filename):
    #~ print filename
    #~ print send_from_directory('/static_resources/', filename)
    #~ path = os.path.abspath('./static_resources/')
    #~ print path + 'css/'
    #~ return send_from_directory(path + 'css/', 'default.css')

# local testing server, add your pages here
@web_app.route("/examples/", methods=['GET'])
def examples():
    """temporary for testing / examples"""
    return make_response(generate.examples())

@web_app.route("/blogs/", methods=['GET'])
def blogs():
    """temporary for testing / examples"""
    return make_response(blog.index())

@web_app.route("/", methods=['GET'])
def index():
    """home page"""
    return make_response(homepage.index())

@web_app.route("/members/", methods=['GET'])
def members_index():
    """list of members"""
    return make_response(members.index())

@web_app.route("/members/<user_id>/<name>", methods=['GET'])
def members_profile(user_id, name):
    """members profile"""
    return make_response(members.profile(user_id, name))

@web_app.route("/chat/", methods=['GET'])
def chat_index():
    """competition page"""
    return make_response(chat.index())

@web_app.route("/contact-us/", methods=['GET'])
def contact_us():
    """Contact page"""
    return make_response(contact_page())

@web_app.route("/contact-us/", methods=['POST'])
def submit_contact_us():
    """Contact page"""
    return make_response(submit_contact_page())

if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000, debug=True)
