import constants as site

from libs.rss_fetcher import feed_reader

from pages import web
from pages import header, footer


def index():
    header()
    web.page.create('blogs')

    web.columns.create()
    web.columns.append('test1')
    web.columns.append('test2')
    web.page.section(web.columns.render())

    web.tiles.create()
    feed = feed_reader(site.rss_feeds)
    for row in feed:
        web.tiles.append(
            title=row.get('title'),
            author=row.get('author'),
            link=row.get('url'),
            image=row.get('image'), 
            date=row.get('date'), 
            description=row.get('description'))
        web.div.append(row)
    web.page.section(web.tiles.render())

    web.template.body.append(web.page.render())
    return footer()
