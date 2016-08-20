from scaffold.core.widget import base_widget_extended

class control(base_widget_extended):
    def create(self, title="Join our mailing list", name=''):
        self.title = title
        self.name = name
        return self

    def render(self):
        htm = '<div %s class="google-groups-signup"><h3>Signup %s</h3>' % (self.get_id(), self.title)
        htm += '<form class="block" name="signup" method="get" action="https://groups.google.com/group/%s/boxsubscribe">' % self.name
        htm += '<label for="groups-email">Email Address</label>'
        htm += '<input id="groups-email" name="email" class="required"/>'
        htm += '<button type="submit" />Subscribe</button>'
        htm += '<a href="http://groups.google.com/group/%s">View Group</a>' % self.name
        htm += '</form><div style="clear:both;"></div><div>'
        return htm
