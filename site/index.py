import os
import sys
import requests
from lxml import etree
from flask import Flask
from flask import make_response

import generate as pages

app = Flask(__name__, static_url_path='/static')

@app.route("/examples/", methods=['GET'])
def examples():
    return make_response(pages.examples())

@app.route("/", methods=['GET'])
def index():
    return make_response(pages.index())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
