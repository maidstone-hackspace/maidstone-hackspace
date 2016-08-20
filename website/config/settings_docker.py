import os
import socket

database = {
                'charset': 'utf8',
                'use_unicode': True,
                'type': 'mysql',
                'host': 'database',
                'user': 'mhackspace',
                'passwd': "mhackspace",
                'db': "maidstone_hackspace",
                'port': 3306}

payment_providers = {
    'paypal': {              
        "mode": "sandbox", # sandbox or live
        'credentials': {
            "mode": "sandbox", # sandbox or live
            "client_id": "AaGlNEvd26FiEJiJi53nfpXh19_oKetteV1NGkBi4DDYZSqBexKVgaz9Lp0SI82gYFSAYpsmxO4iDtxU",
            "client_secret": "EMcIuDJE_VDNSNZS7C7NLi9DEHaDvVu9jlIYyCCHaLmrLuy_VQ6C0bbcRnyF-7B6CcN__Dn6HqUwsgMG"}
        },
    'gocardless':{
        'environment': 'sandbox',
        'credentials': {
            'app_id': 'MNHBS3C4X4ZG211SM70WSS7WCN8B3X1KAWZBKV9S8N6KH2RNH6YZ5Z5865RFD3H6',
            'app_secret': 'NE4NWYDQY4FNN1B47VT9SZ318GPQND130DW7QGQ73JMVTZQZHJQNF23ZFNP48GKV',
            'access_token': 'CJ7G7V36VAH5KVAHTYXD8VE8M4M0S41EQXH2E1HTGV5AN5TAZBER36ERAF4CG2NR',
            'merchant_id': '11QFXD7TTA',
        },
        'redirect_url':'https://test.maidstone-hackspace.org.uk'
    }
}


#~ gocardless_environment = 'sandbox'
#~ gocardless_redirect_uri = 'https://test.maidstone-hackspace.org.uk'
#~ gocardless_credentials = {
    #~ 'app_id': 'MNHBS3C4X4ZG211SM70WSS7WCN8B3X1KAWZBKV9S8N6KH2RNH6YZ5Z5865RFD3H6',
    #~ 'app_secret': 'NE4NWYDQY4FNN1B47VT9SZ318GPQND130DW7QGQ73JMVTZQZHJQNF23ZFNP48GKV',
    #~ 'access_token': 'CJ7G7V36VAH5KVAHTYXD8VE8M4M0S41EQXH2E1HTGV5AN5TAZBER36ERAF4CG2NR',
    #~ 'merchant_id': '11QFXD7TTA'
#~ }


google_calendar_id = 'contact@maidstone-hackspace.org.uk'
google_calendar_api_key = 'AIzaSyA98JvRDmplA9lVLZeKwrs1f2k17resLy0'


google_captcha = {
    'secret': '',
    'site': ''
}

# TODO in scaffold remove when commited
def get_ip_from_hostname(hostname, schema='http'):
    try:
        '%s://%s' % (schema, socket.gethostbyname('nginx'))
    except socket.gaierror:
        return '%s://%s' % (schema, '127.0.0.1')
        
app_domain = 'http://%s' % socket.gethostbyname('nginx')
app_email_template_path = 'templates/email/'
schema = 'https:'
domain = get_ip_from_hostname('nginx')
port = ''
rel_uri = '//' + domain
app_domain = 'http:%s' % rel_uri
app_email_template_path = 'templates/email/'
site_name = 'Maidstone Hackspace'

flask_secret_key = '4466ae96-849f-4fbe-a469-3295bf1a13f5'

oauth_live = False
oauth_conf = {
    'google': {
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://accounts.google.com/o/oauth2/token',
        'scope': [
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile"],
        'client_id': '410132800311-ugnuo356e2l0kbe3h3s3l6tbe1h11qa5.apps.googleusercontent.com',
        'client_secret': 'WlH_ntEc3D8kGghhdh7DrKha',
        'user_uri': 'https://www.googleapis.com/oauth2/v1/userinfo',
        'redirect_uri': app_domain + '/oauth/google'
    },
    'facebook': {
        'auth_uri': 'https://www.facebook.com/dialog/oauth',
        'token_uri': 'https://graph.facebook.com/oauth/access_token',
        'scope': ['public_profile', 'email'],
        'client_id': '212129799138288',
        'client_secret': 'b656db816dc5d7ad13b3e3cb50e3fc78',
        'user_uri': 'https://graph.facebook.com/me?',
        'redirect_uri': app_domain + '/oauth/facebook'
    },
    'github': {
        'auth_uri': 'https://github.com/login/oauth/authorize',
        'token_uri': 'https://github.com/login/oauth/access_token',
        'scope': ['https://api.github.com/user'],
        'client_id': 'aace903b0af45ad72f6c',
        'client_secret': '193faadd5e9400763d0390e2979ce92c49bce93a',
        'user_uri': 'https://api.github.com/user',
        'redirect_uri': app_domain + '/oauth/github'
    }
}

email_server = {
    'username': '',
    'password': '',
    'host': 'mail_server',
    'port': 1025,
    'use_tls': False,
    'from': 'support@maidstone-hackspace.org.uk',
    'to': 'support@maidstone-hackspace.org.uk'}
