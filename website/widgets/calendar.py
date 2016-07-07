from scaffold.core.widget import base_widget

class control(base_widget):

    def create(self, calendar):
        self.calendar = calendar
        return self

    def render(self):
        self.count += 1
        return """<iframe src="https://www.google.com/calendar/embed?src=%s%%40group.calendar.google.com&ctz=Europe/London" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>""" % self.calendar
