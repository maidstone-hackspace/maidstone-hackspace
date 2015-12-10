from scaffold.core.widget import base_widget
from flask import get_flashed_messages

class control(base_widget):
    """rss feed widgets"""
    def create(self):
        return self

    def render(self):
        htm = u'<ul class="messages">'
        for message in get_flashed_messages():
            htm += '<li>%s</li>' % message
        htm += '</ul>' 
        return htm
