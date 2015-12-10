from scaffold.core.widget import base_widget_extended
import requests

class control(base_widget_extended):
    link = None
    action = ""
    includes = []
    script = []

    def create(self, title, image='static/images/close.png'):
        self.image = image
        self.title = title
        return self

    def append(self, content):
        self.content.append(content)
        return self

    def render(self):
        self.count += 1
        return """<div id="ajaxPopup" class="hide" ><div class="closePopup icon-navigation-white icon-navigation-white-ic_close_white_24dp" title="Close popup"></div><div class="content">%s</div></div>""" % ("\n".join(self.content))
