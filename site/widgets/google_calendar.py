from scaffold.core.widget import base_widget_extended
from datetime import datetime
import time
import requests

class control(base_widget_extended):
    contents = []
    def create(self, title="Events", calendar_id=None, api_key=None):
        super(control, self).create()
        url = 'https://www.googleapis.com/calendar/v3/calendars/%s/events?singleEvents=true&maxResults=2&timeMin=%s&key=%s' % (
            calendar_id,
            datetime.now().strftime('%Y-%m-%dT%H:%M:%S-00:00'),
            api_key)
        print url
        date_now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S-00:00')
        response = requests.get('https://www.googleapis.com/calendar/v3/calendars/contact@maidstone-hackspace.org.uk/events?singleEvents=true&maxResults=2&timeMin=%s&key=AIzaSyA98JvRDmplA9lVLZeKwrs1f2k17resLy0' % date_now)
        calendar_data = response.json()
        self.contents = []

        # loop over calendar results, and format for display
        for event in calendar_data.get('items'):
            str_datetime = time.strptime(event.get('start').get('dateTime'), '%Y-%m-%dT%H:%M:%SZ')
            formatted_date = time.strftime('%d %b %Y %H:%M', str_datetime)
            description = event.get('description') + '<br />' if event.get('description') else ''
            location = '<a target="_blank" href="https://www.google.co.uk/maps/search/%s">%s</a>'  % (
                event.get('location'), event.get('location')) if event.get('location') else ''
            self.contents.append((
                event.get('summary')+ '<br />',
                description,
                formatted_date + '<br />' + location))
        return self

    def render(self):
        htm = ''
        for row in self.contents:
            htm += '<li>%s %s %s</li>' % row
        return '''<div class="calendar">
            <ul>%s</ul>
            <span>
                <a class="left but" href="https://calendar.google.com/calendar/render?cid=http://www.google.com/calendar/ical/contact@maidstone-hackspace.org.uk/public/basic.ics">Subscribe</a>
            </span>
            <span>
                <a class="right but" href="https://www.google.com/calendar/embed?src=contact@maidstone-hackspace.org.uk&ctz=Europe/London">View All</a>
            </span></div>''' % htm
