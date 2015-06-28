
page_menu = [
    ('Home', '/'),
    #('About', '#about'),
    ('Competition', '/competition'),
    ('Contact', '#mailing-list-signup')]

banner_images = [
    ('/static/template/images/hackspace-banner.png', '', 'title', 'intro text'),
    ('/static/template/images/example-01.jpg', '', 'title', 'intro text'),
    ('/static/template/images/example-02.jpg', '', 'title', 'intro text')]

tile_images = [
    ('/static/template/images/tile-01.jpg',),
    ('/static/template/images/tile-02.jpg',)]

#required (author,url)
#optional (tags, image)
rss_feeds = [
    {'author':'Simon Ridley',
     'url': 'http://waistcoatforensicator.blogspot.com/feeds/posts/default?alt=rss'},
    {'author':'Mathew Beddow', 'tags': ['tech'], 'url': 'http://www.matthewbeddow.co.uk/?feed=rss2'},
    #{'author':'Oliver Marks', 'url': 'http://www.digitaloctave.co.uk/rss.xml'},
    {'author':'Mike McRoberts', 'url': 'http://thearduinoguy.org/?feed=rss2'}]

kent_hackspace = ['http://www.medwaymakers.co.uk/', 'http://canterbury.hackspace.org.uk/']

email = 'support@maidstone-hackspace.org.uk'

email_server = {
    'user': '',
    'password': '',
    'host': 'email-smtp.us-east-1.amazonaws.com',
    'port': 465,
    'from': 'support@maidstone-hackspace.org.uk',
    'to': 'support@maidstone-hackspace.org.uk'}
