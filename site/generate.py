import os
import sys
import codecs
import argparse

sys.path.append(os.path.abspath('../../../scaffold/'))
sys.path.insert(0,os.path.abspath('../../../scaffold/'))

from scaffold import web
web.load_widgets('widgets')

from libs.rss_fetcher import feed_reader

import constants as site
import pages
from pages import web
from pages import header, footer
from pages import blog
from pages import competition
from pages import donate

from config.settings import *


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
    parser.add_argument('--folder', dest='folder', default='./html/' ,nargs='?', help='output folder')

    #module, function, output file
    pages_list = (
        ('pages.homepage', 'index', 'index.html'),
        ('pages.blog', 'index', 'blog.html'),
        ('pages.chat', 'index', 'chat.html'),
        ('pages.donate', 'index', 'donate.html'),
        ('pages.competition', 'index', 'competition.html'))

    args = parser.parse_args()
    print args.folder

    for module, page, filename in pages_list:
        page_module = __import__(module, globals(), locals(), page)
        with codecs.open(args.folder + '%s' % filename, 'w', "utf-8") as fp:
            try:
                fp.write(getattr(page_module, page)().decode('utf-8'))
                print('Successfully Generated %s%s' % (args.folder, filename))
            except Exception as e:
                print('Failed to Generate %s%s' % (args.folder, filename))
                import traceback
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_tb(exc_traceback, limit=5, file=sys.stdout)
                
