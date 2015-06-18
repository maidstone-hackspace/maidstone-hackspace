import os
import sys
import codecs
import argparse

from scaffold.web import web as html
from scaffold.web import www

import constants as site
from pages import web
from pages import header, footer
from pages import blog


def examples():
    """ page for testing new components"""
    header()

    #this is as simple as you can get
    web.page.section('put some content on the page')
    
    #render to the template
    web.template.body.append(web.page.render())
    
    #finish of the page
    return footer()

def competition():
    """ page for testing new components"""
    header()

    web.page.create(
        web.images.create(
            image='/static/images/competitions/screw_sorting_competition_banner.jpg',
            title="Screw sorting competition banner"
        ).add_attributes('align', 'middle'
        ).add_attributes('style', 'margin:auto;display:block;width:500px;'
        ).render())

    web.paragraph.create(
        """We are some friendly competitions, so if your not sure what to work on consider entering and win some swag.""")
    web.paragraph.append(
        """The First cometition will be to design a device which can sort a jar of screws by size, the winning entry we will attempt to build.""")
    web.page.section(web.paragraph.render())
    
    bullet_list = [
        ("Submit designs by some date here", ),
        ("Images can be design in any software or on a piece of paper but must be submitted as a jpg on the mailing list.", ),
        ("stick figures and crude line drawing are fine, we are not judge your artistic ability.",)]

    web.list.create(ordered=False).set_classes('bullet-list')
    web.list * bullet_list
    web.page.section(web.list.render())

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

    #~ web.tiles.create()
    #~ feed = feed_reader(site.rss_feeds)
    #~ for row in feed:
        #~ print row.get('image')
        #~ web.tiles.append(
            #~ title = row.get('title'),
            #~ author = row.get('author'),
            #~ link = row.get('url'),
            #~ image = row.get('image'), 
            #~ date = row.get('date'), 
            #~ description = row.get('description'))
        #~ web.div.append(row)
    #~ web.page.append(web.tiles.render())

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
        fp.write(competition().decode('utf-8'))

