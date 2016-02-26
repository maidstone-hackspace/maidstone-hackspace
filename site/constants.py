
page_menu = [
    ('Home', '/'),
    ('Chat', '/chat'),
    ('Donate', '/donate'),
    ('Contact', '#mailing-list-signup')]

nav_for_authenticated_user = (
    ('Profile', '/profile'),
    ('Equipment', '/equipment'),
    ('Members', '/members'),
    ('Mailing List', '/mailing-list'),
    ('Logout', '/logout')
)

banner_images = [
    ('/static/images/banners/hackspace-banner.png', '', '', ''),
    ('/static/images/banners/audio_board.jpg', 'Audio board', 'Audio board', ''),
    ('/static/images/banners/microscope.jpg', '', 'Microscope', ''),
    ('/static/images/banners/object_avoiding_robot.jpg', '', 'Object avoiding robot', ''),
    ('/static/images/banners/rocket_camera.jpg', 'Rocket Camera', 'Rocket Camera', '')]
    #~ ('/static/images/example-01.jpg', '', 'title', 'intro text'),
    #~ ('/static/images/example-02.jpg', '', 'title', 'intro text')]

tile_images = [
    ('/static/images/tiles/malta-inn.jpg',),
    ('/static/images/tiles/meetup-malta-inn-31-07-2005.jpg',)]

#required (author,url)
#optional (tags, image)
rss_feeds = [{
        'author':'Simon Ridley',
        'url': 'http://waistcoatforensicator.blogspot.com/feeds/posts/default?alt=rss'
    }, {
        'author':'Mathew Beddow',
        'url': 'http://www.matthewbeddow.co.uk/?feed=rss2',
        'tags': ['tech'], 
    }, {
        'author':'Oliver Marks', 
        'url': 'http://www.digitaloctave.co.uk/rss.xml'
    }, {
        'author':'Ilya Titov', 
        'url': 'http://webboggles.com/feed/'
    }, {
        'author':'Mike McRoberts', 
        'url': 'http://thearduinoguy.org/?feed=rss2'
    }]

kent_hackspace = [
    'http://www.medwaymakers.co.uk/',
    'http://canterbury.hackspace.org.uk/'
]

maker_events = [
    'http://bristolmakerfaire.com/',
    'http://makerfairebrighton.com/',
    'http://makerfaireelephantandcastle.com/',
    'https://www.emfcamp.org/'
]

email = 'support@maidstone-hackspace.org.uk'

email_server = {
    'user': '',
    'password': '',
    'host': 'email-smtp.us-east-1.amazonaws.com',
    'port': 465,
    'from': 'support@maidstone-hackspace.org.uk',
    'to': 'support@maidstone-hackspace.org.uk'}

badge_lookup = {
    1: 'member',
    2: 'backer',
    3: 'teacher',
    4: 'chairman',
    5: 'treasurer',
    6: 'secretary'
}


url_home= '/'
url_profile = '/profile'
url_change_password = '/change_password'
url_change_password = '/reset_password'
url_login = '/login'
