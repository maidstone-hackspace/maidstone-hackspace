from scaffold.core.widget import base_widget_extended
import requests

class control(base_widget_extended):
    contents = []
    def create(self, title="Events", calendar_id=None, api_key=None):
        super(control, self).create()
        response = requests.get('https://www.googleapis.com/calendar/v3/calendars/0rtjmmdbsb8e9351mkip02g8n8@group.calendar.google.com/events?singleEvents=true&maxResults=2&timeMin=2015-12-01T10:00:00-00:00&key=AIzaSyA98JvRDmplA9lVLZeKwrs1f2k17resLy0')
        calendar_data = response.json()
        self.contents = []
        for event in calendar_data.get('items'):
            self.contents.append((
                event.get('summary'), event.get('description'), event.get('location') + ' @ ' + event.get('start').get('dateTime')))
        return self

    def render(self):
        htm = ''
        for row in self.contents:
            htm += '<li>%s</li><li>%s</li><li>%s</li>' % row
        return '''<div class="calendar">
            <ul>%s</ul>
            <span>Subscribe</span><span>View All</span></div>''' % htm


#~ import requests

#~ requests.get('https://www.googleapis.com/calendar/v3/calendars/%s/events?key=%s')
#~ response = requests.get('https://www.googleapis.com/calendar/v3/calendars/0rtjmmdbsb8e9351mkip02g8n8@group.calendar.google.com/events?singleEvents=true&maxResults=2&timeMin=2015-12-01T10:00:00-00:00&key=AIzaSyA98JvRDmplA9lVLZeKwrs1f2k17resLy0')
#~ calendar_data = response.json()
#~ for event in calendar_data.get('items'):
    #~ print event.get('summary')
    #~ print event.get('description')
    #~ print event.get('location')
    #~ print event.get('start').get('dateTime')
