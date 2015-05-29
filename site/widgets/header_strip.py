
#from scaffold.web import web as html
from scaffold.web import www
#from scaffold.web import web as html
#from libs import html as customhtml

class control(www.default.html_ui):
    def create(self, params):
        self.params = params
        return self

    def render(self):
        htm = '<div id="headerstrip"><nav class="navstrip">'
        htm += '<div class="left mini-logo">Maidstone Hackspace</div>'
        htm += '<div id="user_info" class="left">'
        htm += '<div id="newticket"></div>'
        htm += '<div id="username"></div>'
        htm += '</div>'
        htm += '<div class="right">'
        htm += '<div ></div>'
        htm += '</div>'
        htm += '</nav></div>'
        return htm


#~ web.elements['header'] = header()
#web.elements['header_filter'] = header_filter()
#~ web.elements['toolbar_filter'] = toolbar_filter()
