import os

from libs.rss_fetcher import feed_reader

from scaffold.web import web as html
from scaffold.web import www

import constants as site

web = html()
web.load_widgets('widgets')
web.template.create('Maidstone Hackspace', 'Hackspace for Maidstone, kent. for collaberation and discussion for artists, designers, makers, hackers, programmers, tinkerer, professionals and hobbyists.')
web.template.append('<link rel="icon" type="image/png" href="/static/template/images/icon.png">')

#paths
web.document_root = os.path.abspath('./')
web.template.domain = 'http://maidstone-hackspace.org.uk/'
web.template.theme_full_path = os.path.abspath('./static/template') + os.sep
domain = 'http://192.168.21.41:5000/'
image_path = domain + os.sep + 'template' + os.sep + 'images' + os.sep

web.template.css_includes.append('/static/template/default.css')
web.template.css_includes.append('/static/template/js/jquery-ui/themes/base/jquery-ui.css')


def header():
    # logo and social links at very top of the page
    web.header_strip.create({})

    #web.header_strip.social(web.google_plus.create(web.template.domain, plus=True, share=False, comments=False).render())

    web.header_strip.social(web.like.create(url=web.template.domain, plus=True, linkedin=True, facebook=True, twitter='MHackspace').render())
    web.template.body.append(web.header_strip.render())

    # navigation
    web.menu.create('/', 'leftNav')
    web.menu * site.page_menu
    web.template.body.append(web.menu.render())

    # extra javascript libraries
    web.template.javascript_includes.append('<script type="text/javascript" src="/static/js/jquery-2.1.4.min.js"></script>')
    web.template.javascript_includes.append('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular.js"></script>')
    web.template.javascript_includes.append('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular-animate.js"></script>')
    web.template.header.append('<link rel="icon" type="image/png" href="/static/images/favicon.png">')

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
