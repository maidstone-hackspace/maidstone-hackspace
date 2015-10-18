import os
import sys
import requests
from lxml import etree
from flask import Flask
from flask import make_response

import generate
from pages import homepage
from pages import chat
from pages import blog
from pages import competition

web_app = Flask(__name__, static_url_path='/static')

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

#~ @web_app.route("/competition/", methods=['GET'])
#~ def competition_index():
    #~ """competition page"""
    #~ return make_response(competition.index())

@web_app.route("/chat/", methods=['GET'])
def chat_index():
    """competition page"""
    return make_response(chat.index())

if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000, debug=True)
