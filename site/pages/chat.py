import constants as site

from libs.rss_fetcher import feed_reader

from pages import web
from pages import header, footer


def index():
    header()
    web.template.body.append(web.header_strip.create({}).render())
    web.template.body.append(web.menu.render())
    web.page.create(web.title.create('IRC Chat Room').render())
    web.page.create(web.paragraph.create('Pop in and say hi, please be patient users tend to idle, but will like respond if given a chance.').render())
    web.page.section(web.chat.create('maidstone-hackspace').render())
    web.template.body.append(web.page.render())
    return footer()
