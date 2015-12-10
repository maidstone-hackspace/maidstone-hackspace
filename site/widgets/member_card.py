from scaffold.core.widget import base_widget_extended

class control(base_widget_extended):

    def create(self, reference, name):
        super(control, self).create()
        self.reference = reference
        self.name = name
        return self

    def render(self):
        return '''<div id="membercard"><div class="date">Joined 02/12/2015</div><div class="container"><div class="middle"><p>MHS%s</p><p>%s</p></div></div></div>''' % (self.reference, self.name)
