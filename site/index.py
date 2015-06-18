import os
import sys
import requests
from lxml import etree
from flask import Flask
from flask import make_response

import generate as pages


web_app = Flask(__name__, static_url_path='/static')

# local testing server, add your pages here

@web_app.route("/examples/", methods=['GET'])
def examples():
    """temporary for testing / examples"""
    return make_response(pages.examples())

@web_app.route("/blogs/", methods=['GET'])
def blogs():
    """temporary for testing / examples"""
    return make_response(pages.blogs())

@web_app.route("/", methods=['GET'])
def index():
    """home page"""
    return make_response(pages.index())

@web_app.route("/competition/", methods=['GET'])
def competition():
    """competition page"""
    return make_response(pages.competition())

if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000, debug=True)
