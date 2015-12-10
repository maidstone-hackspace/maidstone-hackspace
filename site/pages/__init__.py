import os
import sys

from libs.rss_fetcher import feed_reader

from scaffold.web import webpage as html

import constants as site

from flask.ext.login import current_user

web = html()

web.load_widgets('widgets')
web.template.create('Maidstone Hackspace', 'Hackspace for Maidstone, kent. for collaberation and discussion for artists, designers, makers, hackers, programmers, tinkerer, professionals and hobbyists.')
web.template.append('<link rel="icon" type="image/png" href="/static/images/icon.png">')

#paths
web.document_root = os.path.abspath('./')
web.template.domain = 'http://maidstone-hackspace.org.uk/'
web.template.theme_full_path = os.path.abspath('./static') + os.sep
domain = 'http://192.168.21.41:5000/'
image_path = domain + os.sep + 'images' + os.sep


with web.template as setup:
    setup.persistent_header('<link rel="stylesheet" id="navigationCss" href="/static/css/default.css" media="" type="text/css" />')
    setup.persistent_header('<link rel="stylesheet" id="navigationCss" href="/static/js/jquery-ui/themes/base/jquery-ui.css" media="" type="text/css" />')
    #setup.persistent_header('<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/angular_material/0.9.4/angular-material.min.css">')
    #setup.persistent_header('<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=RobotoDraft:300,400,500,700,400italic">')
    setup.persistent_header('<link rel="stylesheet" id="navigationCss" href="/static/css/sprite-navigation-white.css" media="" type="text/css" />')
    setup.persistent_header('<link rel="stylesheet" id="navigationCss" href="/static/css/sprite-action-white.css" media="" type="text/css" />')
    setup.persistent_header('<link rel="stylesheet" id="navigationCss" href="/static/css/sprite-content-white.css" media="" type="text/css" />')


    setup.persistent_header('<script type="text/javascript" src="/static/js/jquery-2.1.4.min.js"></script>')
    setup.persistent_header('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular.js"></script>')
    setup.persistent_header('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular-animate.js"></script>')
    setup.persistent_header('<script type="text/javascript" src="/static/js/default.js"></script>')

    #setup.persistent_header('<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.3.15/angular-aria.min.js"></script>')
    #setup.persistent_header('<script src="https://ajax.googleapis.com/ajax/libs/angular_material/0.11.2/angular-material.min.js"></script>')

    setup.persistent_header('<link rel="icon" type="image/png" href="/static/images/favicon.png">')


def header(title, description='Maidstone Hackspace is a shared space where artists, designers, makers, hackers, programmers, tinkerers, professionals and hobbyists can work on their projects', url=''):
    # logo and social links at very top of the page
    web.header_strip.create({'logged_in': current_user and current_user.is_authenticated})
    web.header_strip.social(web.like.create(url=web.template.domain + url, plus=True, linkedin=True, facebook=True, twitter='MHackspace').render())
    web.template.body.append(web.header_strip.render())

    # navigation
    web.menu.create('/' + url).set_id('leftNav')
    web.menu * site.page_menu
    if current_user and current_user.is_authenticated:
        web.menu.append('logout', '/logout')
        web.navigation_bar.create(hide=(False if url=='/profile' else True))
        web.navigation_bar.append('Profile', '/profile')
        web.navigation_bar.append('Equipment', '/equipment')
        web.navigation_bar.append('Members', '/members')
        web.navigation_bar.append('Mailing List', '/mailing-list')
        web.template.body.append(web.navigation_bar.render())
    else:
        web.menu.append('login', '/login')
    web.template.body.append(web.menu.render())

def footer():    
    web.footer_content.create().append(
        web.google_groups_signup.create(' and make yourself known','maidstone-hackspace').set_id('mailing-list-signup').render())
    web.template.body.append(web.footer_content.render())
    web.google_analytics.create('maidstone-hackspace.org.uk', 'UA-63373181-1')
    web.template.body.append(web.google_analytics.render())
    return web.render()


class default_page:

    def __enter__(self):
        header()
        return self
