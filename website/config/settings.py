import os 
import constants
import socket
from scaffold.core.data.database import db
from scaffold import web
from libs import mail


schema = 'https:'
domain = '127.0.0.1'
port = '5000'
rel_uri = '//127.0.0.1:5000'
app_domain = 'http:%s' % rel_uri
app_email_template_path = 'templates/email/'
site_name = 'Maidstone Hackspace'

from_email = 'no-reply@maidstone-hackspace.org.uk'

flask_secret_key = '4466ae96-849f-4fbe-a469-3295bf1a13f5'

database = {
                'charset': 'utf8',
                'use_unicode': True,
                'type': 'mysql',
                'host': 'database',
                'user': 'mhackspace',
                'passwd': "mhackspace",
                'db': "maidstone_hackspace",
                'port': 3306}

# secret so not included in default settings
oauth_live = False
oauth_redirect_uri = app_domain + '/oauth'
oauth_conf = {}
payment_providers = {}
google_calendar_id = ''
google_calendar_api_key = ''


if os.environ.get('SERVER_ENVIRONMENT') =='DOCKER':
    if os.path.exists('config/settings_docker.py'):
        print('Using settings for docker enviroment')
        from config.settings_docker import *
else:
    if os.path.exists('config/settings_dev.py'):
        print('Using settings for dev enviroment')
        from config.settings_dev import *

    if os.path.exists('config/settings_testing.py'):
        print('Using settings for test enviroment')
        from config.settings_testing import *

    if os.path.exists('config/settings_live.py'):
        print('Using settings for live enviroment')
        from config.settings_live import *



with web.template as setup:
    #css for jquery, material sprite sheet and custom css
    setup.persistent_header('<link rel="stylesheet" id="navigationCss" href="/static/css/materialize.css" media="" type="text/css" />')
    setup.persistent_header('<link rel="stylesheet" id="navigationCss" href="/static/css/default.css" media="" type="text/css" />')
    setup.persistent_header('<link rel="stylesheet" id="navigationCss" href="/static/js/jquery-ui/themes/base/jquery-ui.css" media="" type="text/css" />')
    setup.persistent_header('<link rel="stylesheet" id="navigationCss" href="/static/css/sprite-navigation-white.css" media="" type="text/css" />')
    setup.persistent_header('<link rel="stylesheet" id="navigationCss" href="/static/css/sprite-action-white.css" media="" type="text/css" />')
    setup.persistent_header('<link rel="stylesheet" id="navigationCss" href="/static/css/sprite-content-white.css" media="" type="text/css" />')

    #javascript, using jquery and angular
    setup.persistent_header('<script type="text/javascript" src="/static/js/jquery-2.2.3.min.js"></script>')
    setup.persistent_header('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular.js"></script>')
    setup.persistent_header('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular-animate.js"></script>')
    setup.persistent_header('<script type="text/javascript" src="/static/js/materialize.js"></script>')
    setup.persistent_header('<script type="text/javascript" src="/static/js/default.js"></script>')

    #other favicon etc
    setup.persistent_header('<link rel="icon" type="image/png" href="/static/images/favicon.png">')

    setup.persistant_uris(
        schema=schema,
        domain=domain,
        port=port)

db.config(database)
mail.sendmail.set_server(email_server)
