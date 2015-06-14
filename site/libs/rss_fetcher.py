import os
import sys
import lxml
import pytz
import datetime
import requests
import functools
import requests.exceptions


#from lxml import etree, objectify
from lxml.html.clean import Cleaner

namespaces = {
    'atom': "http://www.w3.org/2005/Atom",
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
    'content': "http://purl.org/rss/1.0/modules/content/",
    'wfw': "http://wellformedweb.org/CommentAPI/",
    'dc': "http://purl.org/dc/elements/1.1/",
    'atom': "http://www.w3.org/2005/Atom",
    'sy': "http://purl.org/rss/1.0/modules/syndication/",
    'slash': "http://purl.org/rss/1.0/modules/slash/"
}


#~ import zlib
#~ 
#~ READ_BLOCK_SIZE = 1024 * 8
#~ def decompress_stream(fileobj):
    #~ result = StringIO()
#~ 
    #~ d = zlib.decompressobj(16 + zlib.MAX_WBITS)
    #~ for chunk in iter(partial(response.raw.read, READ_BLOCK_SIZE), ''):
        #~ result.write(d.decompress(chunk))
#~ 
    #~ result.seek(0)
    #~ return result


#~ parser = etree.XMLParser(remove_blank_text=True, ns_clean=True)
#~ tree = etree.parse(metadata, parser)
#~ root = tree.getroot()

from email.utils import parsedate_tz, mktime_tz

class feed_reader:
    #create the html cleaner, this is to clean out unwanted html tags in the description text
    html_cleaner = Cleaner()
    html_cleaner.javascript = True 
    html_cleaner.style = True
    html_cleaner.remove_tags = ['script', 'iframe', 'link', 'style']
    filter_by_date = datetime.datetime.now() - datetime.timedelta(days=int(1.5*365)) #  1 and a half years ago
    #html_cleaner.allow_tags = ['script', 'iframe', 'link', 'style']
    #html_cleaner.kill_tags = ['script', 'iframe', 'link', 'style']
    
    def __init__(self, feed_details, timeout=5):
        self.results = {}
        parser = lxml.etree.XMLParser(remove_blank_text=True, ns_clean=True, encoding='utf-8')
        for feed_info in feed_details:
            self.url = feed_info.get('url')
            self.author = feed_info.get('author')
            self.tags = feed_info.get('tags')
            if feed_info.get('url').startswith('http:'):
                response = requests.get(feed_info.get('url'), stream=True, timeout=timeout)
                if response.headers.get('content-encoding') == 'gzip':
                    response.raw.read = functools.partial(response.raw.read, decode_content=True)
                self.feed = lxml.etree.parse(response.raw, parser)
            else:
                fp = open(feed_info.get('url'), 'r')
                self.feed = lxml.etree.parse(fp, parser)
            
            self.feed = self.feed.getroot()
            self.parse_feed()

    def convert_rfc822_to_datetime(self, rfcdate):
        if len(rfcdate):
            parsed_rfcdate = parsedate_tz( rfcdate )
            if not parsed_rfcdate:
                return None
            return datetime.datetime.fromtimestamp(
                mktime_tz(parsed_rfcdate), pytz.utc ).replace(tzinfo=None)
        return None

    def clean_up_text(self, text):
        """strip out any dirty tags like <script> they may break the sites"""
        return self.html_cleaner.clean_html(text)

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

    def fetch_node_attribute(self, node, names, attribs, default):
        result = node.xpath('./%s' % name)
        if result:
            return result.get(atrribs, '')
        else:
            return default

    def format_author(self, author):
        """extract the authors name from the author text node"""
        return author.split('(')[-1].strip(')')

    def filter(self, node, tags=None):
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
            if date > self.filter_by_date and self.filter(item):
                self.filter(item)
                self.results[date] = {
                    'title': self.fetch_node_text(item, 'title'),
                    'date': date,
                    'url': self.fetch_node_text(item, 'link'),
                    'author': self.format_author(self.fetch_node_text(item, 'author', self.author)),
                    'image': self.fetch_node_text(item, 'image'),
                    'description': self.clean_up_text(self.fetch_node_text(item, 'description'))}

    def __iter__(self):
        """return results ordered by date"""
        for order in sorted(self.results.keys(), reverse=True):
            #print str(self.results[order]['date']) + ' - ' + self.results[order]['author'] + ' - ' + self.results[order]['title']
            yield self.results[order]
        
rss_feeds = [
    {'author':'Simon Ridley', 'url': 'http://waistcoatforensicator.blogspot.com/feeds/posts/default?alt=rss'},
    {'author':'Mathew Beddow', 'tags': ['tech'], 'url': 'http://www.matthewbeddow.co.uk/?feed=rss2'},
    {'author':'Mike McRoberts', 'url': 'http://thearduinoguy.org/?feed=rss2'}]

#~ import .constants
test = feed_reader(rss_feeds)
for item in test:
    pass
