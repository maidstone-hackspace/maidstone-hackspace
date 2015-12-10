import os
import sys
sys.path.append(os.path.abspath('../'))
from urlparse import urlparse
from StringIO import StringIO
from PIL import Image
import requests
from libs.rss_fetcher import feed_reader
import constants as site


feed = feed_reader(site.rss_feeds)
feed.enable_date_filter = False
count = 0
for row in feed:
    full_url = row.get('image')
    if full_url:
        url = urlparse(full_url)
        ext = os.path.split(url.path)[-1].split('.')[-1]
	img = requests.get(full_url)
        i = Image.open(StringIO(img.content))
        i.save('images/blog_image_%s.%s' % (str(count),  ext))
        count += 1
