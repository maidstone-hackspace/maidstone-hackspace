import argparse

import os
import sys
import requests
import requests.exceptions
from lxml import etree
import lxml

from settings import *
from scaffold.web import web as html
from scaffold.web import www

import constants as site

import codecs

from libs.rss_fetcher import feed_reader

web = html()
web.load_widgets('widgets')
web.template.create('Maidstone Hackspace', 'Hackspace for Maidstone, kent. for collaberation and discussion for artists, designers, makers, hackers, programmers, tinkerer, professionals and hobbyists.')
web.template.append('<link rel="icon" type="image/png" href="/static/template/images/icon.png">')

#paths
web.document_root = os.path.abspath('./')
web.template.theme_full_path = os.path.abspath('./static/template') + os.sep
domain = 'http://192.168.21.41:5000/'
image_path = domain + os.sep + 'template' + os.sep + 'images' + os.sep

web.template.css_includes.append('/static/template/default.css')
web.template.css_includes.append('/static/template/js/jquery-ui/themes/base/jquery-ui.css')
#~ web.template.javascript_includes.append('/static/template/js/jquery-ui/themes/base/jquery-ui.css')

def todict(data):
    new_dict = {}
    for key, value in data.items():
        new_dict[key] = value
    return new_dict

def dict_to_list(data, keys):
    return [data.get(k) for k in keys]

#~ class page:
    #~ def __enter__(self):
        #~ header()
    #~ 
    #~ def __exit(self):
        #~ footer()

def header():
    web.menu.create('/', 'leftNav')
    web.menu * site.page_menu
    web.template.body.append(web.header_strip.create({}).render())
    web.template.body.append(web.menu.render())
    web.template.javascript_includes.append('<script type="text/javascript" src="/static/js/jquery-2.1.4.min.js"></script>')
    web.template.javascript_includes.append('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular.js"></script>')
    web.template.javascript_includes.append('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular-animate.js"></script>')


def footer():    
    web.footer_content.create().append(
        web.google_groups_signup.create(' and make yourself known','maidstone-hackspace').set_id('mailing-list-signup').render())
    web.template.body.append(web.footer_content.render())
    web.google_analytics.create('maidstone-hackspace.org.uk', 'UA-63373181-1')
    web.template.body.append(web.google_analytics.render())
    return web.render()

def examples():
    """ page for testing new components"""
    header()
    web.page.create('examples')
    web.twitter_feed.create(username='MHackspace', widget_id='606798560374484992')
    web.page.section(web.twitter_feed.render())

    web.page.append(
        web.google_groups.create(
            ' and make yourself known','maidstone-hackspace'
        ).set_id('mailing-list').render()
    )

    web.tiles.create()
    #~ feed = feed_reader('')
    

    feed = feed_reader(site.rss_feeds)

    for row in feed:
        print row
        print type(row.get('description'))
        web.tiles.append(
            title = '%s By %s' %(row.get('title'), row.get('author')),
            link = row.get('url'),
            image = row.get('image'), 
            description = row.get('description'))
        web.div.append(row)
    web.page.append(web.tiles.render())

    web.template.body.append(web.page.render())
    return footer()

def blogs():
    """ page for testing new components"""
    header()
    web.page.create('blogs')

    web.tiles.create()
    feed = feed_reader(site.rss_feeds)

    for row in feed:
        print row.get('image')
        web.tiles.append(
            title = row.get('title'),
            author = row.get('author'),
            link = row.get('url'),
            image = row.get('image'), 
            date = row.get('date'), 
            description = row.get('description'))
        web.div.append(row)
    web.page.section(web.tiles.render())

    web.template.body.append(web.page.render())
    return footer()

def index():
    header()

    web.template.body.append(web.header_strip.create({}).render())
    web.template.body.append(web.menu.render())

    web.page.create('')
    web.page.section(
        web.images.create(
            '/static/template/images/tile-01.jpg'
        ).append(
            '/static/template/images/tile-01.jpg'
        ).set_classes('tile-right').render())
    web.banner_slider.reset()
    print site.banner_images
    web.banner_slider * site.banner_images
    
    web.page.append(web.banner_slider.render())

    web.page.section(web.title.create('Introduction').render())

    web.paragraph.create(
        """Hackspaces are a shared space where artists, designers, makers, hackers, programmers, tinkerers, professionals and hobbyists
        can work on their projects, share knowledge and collaborate.""")

    web.paragraph.append(
        """We are in the process of developing Maidstone Hackspace. We're previous members of <span class="info" title="Innovation center medway prototype">(ICMP)</span> and looking to form a new space in the future.
        At the moment, communication is via google groups, email, and the website. If you're at all intrested please join our <a href="#mailing-list-signup">mailing list</a>
        and make yourself known!""")
    web.page.section(web.paragraph.render())

    web.page.section(web.title.create('Proposed activities').render())

    bullet_list = []
    bullet_list.append(
        ("""Workshop on building a mobile application which can run on ios and android, potentially game oriented for a bit of fun, but open to suggestions.""",))
    bullet_list.append(
        ("""Build an interactive splash screen to feature on this site.""",))
    bullet_list.append(
        (web.link.create('Suggest a new activity', 'Suggest a new activity', '#mailing-list-signup').render(),))

    web.list.create(ordered=False).set_classes('bullet-list')
    web.list * bullet_list
    web.page.append(web.list.render())

    web.div.create('').set_classes('panel')

    web.twitter_feed.create(username='MHackspace', widget_id='606798560374484992')
    web.page.append(web.twitter_feed.render())
    web.template.body.append(web.page.render())

    return footer()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Generate static pages')
    parser.add_argument('--folder', dest='folder', nargs='?', help='output folder')
    #~ args = parser.parse_args()
    #~ print(args.accumulate(args.integers))

    with codecs.open('./html/index.html', 'w', "utf-8") as fp:
        fp.write(index().decode('utf-8'))
    #~ with open('./html/examples.html', 'w') as fp:
        #~ fp.write(examples())
    with codecs.open('./html/blog.html', 'w', "utf-8") as fp:
        fp.write(blogs().decode('utf-8'))

#~ file = codecs.open("lol", "w", "utf-8")
#~ file.write(u'\ufeff')
#~ file.close()
