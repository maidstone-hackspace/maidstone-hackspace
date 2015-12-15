import os
import sys
import requests
from lxml import etree
from flask import Flask
from flask import make_response
from flask.ext.login import LoginManager, login_required

sys.path.append(os.path.abspath('../../../scaffold/'))
sys.path.insert(0,os.path.abspath('../../../scaffold/'))

from config import settings
import generate
from pages import homepage
from pages import chat
from pages import blog
from pages import competition

from pages import members

from pages.donate import donate_pages
from pages.google_groups import google_groups_pages
from pages.equipment import equipment_pages
from pages.profile import profile_pages
from authorize import authorize_pages, login_manager

web_app = Flask(__name__, static_url_path='/static')
web_app.config['PROPAGATE_EXCEPTIONS'] = True
web_app.secret_key = settings.flask_secret_key
login_manager.init_app(web_app)

web_app.register_blueprint(authorize_pages)
web_app.register_blueprint(equipment_pages)
web_app.register_blueprint(profile_pages)
web_app.register_blueprint(google_groups_pages)
web_app.register_blueprint(donate_pages)


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

#~ @login_required
#~ @web_app.route("/equipment", methods=['GET'])
#~ def equipment_view():
    #~ """home page"""
    #~ return make_response(equipment.index())

#~ @login_required
#~ @web_app.route("/equipment/edit/<request_id>/", methods=['GET'])
#~ def equipment_edit_view(request_id):
    #~ """home page"""
    #~ return make_response(equipment.edit(request_id))

#~ @login_required
#~ @web_app.route("/equipment", methods=['POST'])
#~ def equipment_submit():
    #~ """home page"""
    #~ equipment.insert()
    #~ return make_response(equipment.index())

#~ @web_app.route("/donate/", methods=['GET'])
#~ def donate_index():
    #~ """list of members"""
    #~ return make_response(donate.index())

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

if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000, debug=True)
