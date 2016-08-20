import constants as site
from libs.image_fetcher import save_remote_image
from config.settings import google_calendar_id, google_calendar_api_key, app_domain

from scaffold.readers.rss_reader import feed_reader
from scaffold import web
from pages import header, footer


def index():
    web.template.create('Maidstone Hackspace')
    header('Maidstone Hackspace Homepage')
    web.page.create('').set_classes('page col s10 offset-s1')
    web.page.section(
        web.div.create(
            web.google_calendar.create(
                calendar_id=google_calendar_id,
                api_key=google_calendar_api_key).render()
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

    #~ web.div.create('').set_classes('panel')

    # fetch the rss feeds from the various blogs for the homepage
    web.columns.create()
    feed = feed_reader(site.rss_feeds)
    
    
    web.tiles.create()
    for row in feed:
        row['image'] = save_remote_image(row.get('image'), domain=app_domain + '/')
        
        web.tiles.append(
                title = row.get('title'),
                author = row.get('author'),
                link = row.get('url'),
                image = row.get('image'), 
                date = row.get('date'), 
                description = row.get('description')).render()
        #~ web.columns.append(
            #~ )
    web.page.append(web.div.create(web.tiles.render()).set_classes('row').render())
    web.template.body.append(web.page.render())

    return footer()
