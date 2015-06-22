import os
import sys
import codecs
import argparse

from scaffold.web import web as html
from scaffold.web import www

from libs.rss_fetcher import feed_reader

import constants as site
from pages import web
from pages import header, footer
from pages import blog
from pages import competition


def examples():
    """ page for testing new components"""
    header()

    #this is as simple as you can get
    web.page.section('put some content on the page')
    
    #render to the template
    web.template.body.append(web.page.render())
    
    #finish of the page
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

    bullet_list = [
        ("Workshop on building a mobile application which can run on ios and android,"
        "potentially game oriented for a bit of fun, but open to suggestions.", ),
        ("Build an interactive splash screen to feature on this site.",),
        (web.link.create('Suggest a new activity', 'Suggest a new activity', '#mailing-list-signup').render(),)]

    web.list.create(ordered=False).set_classes('bullet-list')
    web.list * bullet_list
    web.page.append(web.list.render())

    web.div.create('').set_classes('panel')

    web.twitter_feed.create(username='MHackspace', widget_id='606798560374484992')

    
    web.page.append(web.twitter_feed.render())

    feed = feed_reader(site.rss_feeds)
    
    web.columns.create()
    for row in feed:
        web.tiles.create()
        web.columns.append(
            web.tiles.append(
                title = row.get('title'),
                author = row.get('author'),
                link = row.get('url'),
                image = row.get('image'), 
                date = row.get('date'), 
                description = row.get('description')).render())
    web.page.append(web.columns.render())

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
        fp.write(blog.index().decode('utf-8'))

    with codecs.open('./html/competition.html', 'w', "utf-8") as fp:
        fp.write(competition.index().decode('utf-8'))

