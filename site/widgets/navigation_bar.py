from scaffold.core.widget import base_widget

class control(base_widget):
#~ class control(base_widget):
    script = ['$document).ready(function(){$()});']
    
    def create(self, hide=True):
        super(control, self).create()
        self.hide = hide
        self.content = []
        return self

    def append(self, title, link):
        self.content.append((title, link))

    def render(self):
            
        htm = '<div id="member_navigation" %s><ul>' % ('style="display:none;"' if self.hide is True else '')
        for title, link in self.content:
            htm += '<li><a href="%s" title="%s">%s</a></li>' %(link, title, title)
        htm += '</ul></div>'
        return htm
