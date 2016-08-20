"""https://developers.google.com/recaptcha/docs/verify"""

from requests import post
from config.logger import log

def verify_captcha(secret, response, remoteip=''):
    try:
        response = post(
            'https://www.google.com/recaptcha/api/siteverify',
            {'secret': secret,
            'response': response,
            'remoteip': remoteip})
        json = response.json()
    except:
        log.error('Failed to get capture json response from google')
        return False
    return json.get('success')

