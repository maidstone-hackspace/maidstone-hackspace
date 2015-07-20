import constants as site

from libs.rss_fetcher import feed_reader

from pages import web
from pages import header, footer


def index():
    header('Maidstone Hackspace Forge')
    return footer()
