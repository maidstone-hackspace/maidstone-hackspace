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

# normally you will abstract the html into the widgets folder so its reusable
# to keep things as simple as possibler for everyone you can bypass and render you html direct
# either to tha page web.page.section or to web.template.body
# This is the simplest way to make a page
def simple_page():
    web.template.create('Maidstone Hackspace')
    header('Maidstone Hackspace Homepage')
    
    # render to a page in this way
    web.page.create('Page title ')
    web.page.section('<p>Page Body<p>')
    web.template.body.append(web.page.render())
    
    # render direct to the template body in this way
    data = {
        'first_value': 'value from where ever',
        'second_value': 'value from where ever'}

    web.template.body.append("""
        <div>some content here</div>
        <p>paragrph or any other html you want to place in here</p>
        <span>{first_value}</span>
        <span>{second_value}</span>
    """.format(*data))
    return footer()
