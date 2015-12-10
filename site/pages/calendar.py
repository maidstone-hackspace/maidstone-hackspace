import constants as site

from libs.rss_fetcher import feed_reader

from pages import web
from pages import header, footer


def index():
    header('Maidstone Hackspace Calendar')
    web.template.body.append(web.header_strip.create({}).render())
    web.template.body.append(web.menu.render())
    
    web.calendar.create('https://www.google.com/calendar/feeds/0rtjmmdbsb8e9351mkip02g8n8%40group.calendar.google.com/public/basic')
    
    web.page.create(web.title.create('IRC Chat Room').render())
    web.page.create(web.paragraph.create('Pop in and say hi, please be patient users tend to idle and will respond when they get a chance.').render())
    web.page.section(web.chat.create('maidstone-hackspace').render())
    web.template.body.append(web.page.render())
    return footer()
