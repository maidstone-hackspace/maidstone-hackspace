import constants as site

from libs.rss_fetcher import feed_reader

from pages import web
from pages import header, footer


def twitter():
    web.template.create('Maidstone Hackspace')
    header('Maidstone Hackspace Homepage')
    web.page.create('')
    web.twitter_feed.create(username='MHackspace', widget_id='606798560374484992')
    web.page.section(
        web.twitter_feed.render())
    web.template.body.append(web.page.render())
    return footer()
