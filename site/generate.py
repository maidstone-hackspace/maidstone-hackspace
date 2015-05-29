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

def todict(data):
    new_dict = {}
    for key, value in data.items():
        new_dict[key] = value
    return new_dict

def dict_to_list(data, keys):
    return [data.get(k) for k in keys]

class feed_reader:
    def __init__(self, url):
        #~ self.feed = requests.get(url, stream=True)
        fp = open('rss_example.xml', 'r')
        self.feed = etree.parse(fp)
        self.feed = self.feed.getroot()
        #~ self.channel = self.feed.xpath('.//item')
        #~ print self.channel
        
            #for channel in feed.xpath(".//item"):
        self.title = self.feed.xpath('./channel/title/text()')[-1]
        self.link = self.feed.xpath('./channel/link/text()')[-1]
        self.description = self.feed.xpath('./channel/description/text()')[-1]

        self.channel_image = self.feed.xpath('.//image/url/text()')[-1]
        self.channel_image_title = self.feed.xpath('.//image/title/text()')[-1]
        self.channel_image_link = self.feed.xpath('.//image/link/text()')[-1]

    def __iter__(self):
        for item in self.feed.xpath('.//item'):
            title = item.xpath('./title/text()')
            link = item.xpath('./link/text()')
            description = item.xpath('./description/text()')
            yield title, link, description

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
    web.google_analytics.create('maidstone-hackspace.org.uk', 'UA-63373181-1')

def footer():    
    web.template.body.append(web.footer_content.render())
    web.google_analytics.create('maidstone-hackspace.org.uk', 'UA-63373181-1')
    web.template.body.append(web.google_analytics.render())
    return web.render()

def examples():
    """ page for testing new components"""
    header()
    print 'examples page'
    #~ web.template.create('examples')
    web.page.create('examples')
    web.twitter_feed.create('olymk2')
    web.page.section(web.twitter_feed.render())
    footer()

    web.template.body.append(web.page.render())
    with open('examples.html', 'w') as fp:
        fp.write(footer())

def index():
    header()

    web.menu.create('/', 'leftNav')
    web.menu * site.page_menu

    web.template.body.append(web.header_strip.create({}).render())
    web.template.body.append(web.menu.render())

    web.page.create('')
    web.page.section(web.images.create('/static/template/images/tile-01.jpg').set_classes('tile-right').append('/static/template/images/tile-01.jpg').render())
    web.banner_slider.reset()
    web.banner_slider * site.banner_images
    
    web.page.append(web.banner_slider.render())

    web.page.section(web.title.create('Introduction').render())

    web.paragraph.create(
        """Hackspaces are a shared space where artists, designers, makers, hackers, programmers, tinkerers, professionals and hobbyists
        can work on their projects, share knowledge and collaborate.""")

    web.paragraph.append(
        """We are in the process of developing Maidstone Hackspace. We're previous members of <span class="info" title="Innovation center medway prototype">(ICMP)</span> and looking to form a new space in the future.
        At the moment, communication is via google groups, email, and the website. If you're at all intrested please join our <a href="#mailing-list">mailing list</a>
        and make yourself known!""")
    web.page.section(web.paragraph.render())

    web.page.section(web.title.create('Proposed activities').render())

    bullet_list = []
    bullet_list.append(
        ("""Workshop on building a mobile application which can run on ios and android, potentially game oriented for a bit of fun, but open to suggestions.""",))
    bullet_list.append(
        ("""Build an interactive splash screen to feature on this site.""",))
    bullet_list.append(
        (web.link.create('Suggest a new activity', 'Suggest a new activity', '#mailing-list').render(),))


    
    web.list.create(ordered=False).set_classes('bullet-list')
    web.list * bullet_list
    web.page.append(web.list.render())

    web.footer_content.create().append(
        web.google_groups.create(' and make yourself known','maidstone-hackspace').set_id('mailing-list').render())

    web.div.create('').set_classes('panel')

    web.tiles.create()
    #~ for project in get_users_projects({'user_id': data.get('user_id')}):
        #~ web.tiles.append(project.get('title'), project.get('id'))
    #~ return web.tiles.render()

    feed = feed_reader('')
    for row in feed:
        web.tiles.append(
            title = feed.title,
            link = feed.link,
            image = feed.channel_image, 
            description = 'lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum.')
        web.div.append(str(row))
    web.page.append(web.tiles.render())
    
    web.page.append(web.twitter_feed.render())
    
    web.template.body.append(web.page.render())

    #~ web.google_analytics.create('maidstone-hackspace.org.uk', 'UA-63373181-1')
    #~ web.template.body.append(web.google_analytics.render())
    
    #~ with open('index.html', 'w') as fp:
        #~ fp.write()
    return footer()

parser = argparse.ArgumentParser(description = 'Generate static pages')
#~ parser.add_argument('--help', help='Return help')
#~ parser.add_argument('--folder', dest='folder', nargs='?', help='output folder')
#~ args = parser.parse_args()
#~ print(args.accumulate(args.integers))

index()
examples()
