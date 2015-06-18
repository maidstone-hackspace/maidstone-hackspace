import os
from scaffold.web import www

class control(www.default.html_ui): 
    """Image cycle widgets"""
    buttons = []
    count = 0
    
    with open(os.path.abspath('./widgets/banner_slider.js')) as fp:
        js = [fp.read()]
    
    def create(self):
        self.reset()

    def reset(self):
        self.content = []

    def append(self, text):
        self.content.append(u'<div class="content">%s</div>' % (text))

    def render(self):   
        return u"".join(self.content)
