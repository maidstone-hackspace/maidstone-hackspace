import constants as site

from libs.rss_fetcher import feed_reader

from pages import web
from pages import header, footer


def index():
    web.template.create('Maidstone Hackspace')
    header('Maidstone Hackspace Homepage')
    web.page.create('')
    web.page.section(
        web.div.create(
            web.images.create(
                '/static/template/images/tile-01.jpg'
            ).append(
                '/static/template/images/tile-01.jpg'
            ).render()
        ).set_classes('tile-right tile-image').render())
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
        (web.link.create('Suggest a new activity', 'Suggest a new activity', 'https://groups.google.com/forum/#!forum/maidstone-hackspace').render(),)]

    web.list.create(ordered=False).set_classes('bullet-list')
    web.list * bullet_list
    web.page.append(web.list.render())

    web.div.create('').set_classes('panel')

    web.twitter_feed.create(username='MHackspace', widget_id='606798560374484992')
    feed = feed_reader(site.rss_feeds)
    
    web.columns.create()
    web.columns.append(web.twitter_feed.render())
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
