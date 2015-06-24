import os
import sys
import codecs
import argparse

from scaffold.web import web as html
from scaffold.web import www

from libs.rss_fetcher import feed_reader

import constants as site
import pages
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate static pages')
    parser.add_argument('--folder', dest='folder', nargs='?', help='output folder')

    #module, function, output file
    pages_list = (
        ('pages.homepage', 'index', 'index.html'),
        ('pages.blog', 'index', 'blog.html'),
        ('pages.chat', 'index', 'chat.html'),
        ('pages.competition', 'index', 'competition.html'))

    for module, page, filename in pages_list:
        page_module = __import__(module, globals(), locals(), page)
        with codecs.open('./html/%s' % filename, 'w', "utf-8") as fp:
            try:
                fp.write(getattr(page_module, page)().decode('utf-8'))
                print('Successfully Generated ./html/%s' % filename)
            except:
                print('Failed to Generate ./html/%s' % filename)
