import os
import sys
import lxml
import pytz
import StringIO
import datetime
import requests
import functools
import requests.exceptions

from lxml.html.clean import Cleaner

namespaces = {
    'openSearch': "http://a9.com/-/spec/opensearchrss/1.0/",
    'blogger': "http://schemas.google.com/blogger/2008",
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'slash': "http://purl.org/rss/1.0/modules/slash/",
    'content': "http://purl.org/rss/1.0/modules/content/",
    'taxo': "http://purl.org/rss/1.0/modules/taxonomy/",
    'dc': "http://purl.org/dc/elements/1.1/",
    'syn': "http://purl.org/rss/1.0/modules/syndication/",
    'admin': "http://webns.net/mvcb/",
    'feedburner': "http://rssnamespace.org/feedburner/ext/1.0",
    'wfw': "http://wellformedweb.org/CommentAPI/",
    'dc': "http://purl.org/dc/elements/1.1/",
    'atom': "http://www.w3.org/2005/Atom",
    'sy': "http://purl.org/rss/1.0/modules/syndication/",
    'slash': "http://purl.org/rss/1.0/modules/slash/",
    'atom': "http://www.w3.org/2005/Atom",
    'content': "http://purl.org/rss/1.0/modules/content/",
    'media': "http://search.yahoo.com/mrss/",
}


from email.utils import parsedate_tz, mktime_tz

class feed_reader:
    """parse a list of feeds and return details as dictionary data"""
    #create the html cleaner, this is to clean out unwanted html tags in the description text
    html_cleaner = Cleaner()
    html_cleaner.javascript = True 
    html_cleaner.style = True
    html_cleaner.remove_tags = ['script', 'iframe', 'link', 'style', 'img']

    filter_by_date = datetime.datetime.now() - datetime.timedelta(days=int(1.5*365)) #  1 and a half years ago

    html_img_cleaner = Cleaner(allow_tags=['img'], remove_unknown_tags=False)
    html_img_cleaner.allow_tags = ['img']

    html_parser = lxml.etree.HTMLParser()
    xml_parser = lxml.etree.XMLParser(remove_blank_text=True, ns_clean=True, encoding='utf-8')

    def __init__(self, feed_details, timeout=5):
        self.results = {}
        for feed_info in feed_details:
            self.url = feed_info.get('url')
            self.author = feed_info.get('author')
            self.tags = feed_info.get('tags')
            if feed_info.get('url').startswith('http:'):
                response = requests.get(feed_info.get('url'), stream=True, timeout=timeout)
                if response.headers.get('content-encoding') == 'gzip':
                    response.raw.read = functools.partial(response.raw.read, decode_content=True)
                try:
                    self.feed = lxml.etree.parse(response.raw, self.xml_parser)
                except:
                    continue
            else:
                with open(os.path.abspath(feed_info.get('url')), 'r') as file_stream:
                    try:
                        self.feed = lxml.etree.parse(file_stream, self.xml_parser)
                    except:
                        continue
            
            self.feed = self.feed.getroot()
            
            # rss feed defaults
            self.channel_image = self.fetch_node_text(self.feed, 'channel/image/url', '')

            self.parse_feed()

    def convert_rfc822_to_datetime(self, rfcdate):
        """rss uses rfc822 dates so lets convert them to datetime for use later"""
        if len(rfcdate):
            parsed_rfcdate = parsedate_tz(rfcdate)
            if not parsed_rfcdate:
                return None
            return datetime.datetime.fromtimestamp(
                mktime_tz(parsed_rfcdate), pytz.utc).replace(tzinfo=None)
        return None

    def clean_up_text(self, text):
        """strip out any dirty tags like <script> they may break the sites"""
        return self.html_cleaner.clean_html(text)

    def fetch_image_from_node_text(self, text):
        description = lxml.etree.parse(StringIO.StringIO(text), self.html_parser)
        for image in description.xpath('.//img'):
            return image.get('src')
        return None

    def fetch_image(self, node):
        """Try and get an image from an item in the feed, use various fall back methods"""
        image = node.xpath('media:thumbnail', namespaces=namespaces)
        if image:
            return image[0].get('url', '')

        # no media:thumbnail so lets try and grab an image from content:encoded
        image = node.xpath('content:encoded', namespaces=namespaces)
        if image:
            image = self.fetch_image_from_node_text(image[0].text)
            if image:
                return image

        # final attempt at getting an image from the item using description
        result = self.fetch_node_text(node, 'description')
        if result:
            image = self.fetch_image_from_node_text(result)
            if image:
                return image

        # no image so lets fall back to the channel image if it exists
        return self.channel_image

    def fetch_node_text(self, node, name, default=''):
        """fetch the text from the node we are given, we are working in unicode
        so decode byte strings to unicode""" 
        result = node.xpath('./%s' % name)
        if result:
            if type(result[-1].text) is str:
                return result[-1].text.decode('utf8')
            else:
                return result[-1].text
        else:
            return default

    def fetch_node_attribute(self, node, name, attribs, default):
        result = node.xpath('./%s' % name)
        if result:
            return result.get(attribs, '')
        else:
            return default

    def format_author(self, author):
        """extract the authors name from the author text node"""
        return author.split('(')[-1].strip(')')

    def filter_by_tags(self, node, tags=None):
        """filter the feed out by category tag, if no tags assume its pre filtered"""
        if self.tags is None:
            return True
        for category in node.xpath('./category', namespaces=namespaces):
            if category.text.lower() in self.tags:
                return True
        return False

    def parse_feed(self):
        """Parse the items in the feed, filter out bad data and put in defaults"""
        for item in self.feed.xpath('.//item', namespaces=namespaces):
            date = self.convert_rfc822_to_datetime(self.fetch_node_text(item, 'pubDate'))
            if date > self.filter_by_date and self.filter_by_tags(item):
                self.results[date] = {
                    'title': self.fetch_node_text(item, 'title'),
                    'date': date,
                    'url': self.fetch_node_text(item, 'link'),
                    'author': self.format_author(self.fetch_node_text(item, 'author', self.author)),
                    'image': self.fetch_image(item),
                    'description': self.clean_up_text(self.fetch_node_text(item, 'description'))}

    def __iter__(self):
        """return results ordered by date"""
        for order in sorted(self.results.keys(), reverse=True):
            #print str(self.results[order]['date']) + ' - ' + self.results[order]['author'] + ' - ' + self.results[order]['title']
            yield self.results[order]

if __name__ == "__main__":
    rss_tests = [
        {'author': 'Mike McRoberts', 'url': './rss_invalid.xml'},
        {'author': 'Mike McRoberts', 'url': './rss_no_tags.xml'}]

    test = feed_reader(rss_tests)

