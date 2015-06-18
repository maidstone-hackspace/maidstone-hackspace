from scaffold.core.widget import base_widget

class control(base_widget):
    def create(self, params):
        self.params = params
        self.social_html = []
        return self

    def social(self, htm):
        self.social_html.append(htm)

    def render(self):
        htm = '<div id="headerstrip"><nav class="navstrip">'
        htm += '<div class="left mini-logo">Maidstone Hackspace</div>'
        htm += '<div class="social">'
        htm += "".join(self.social_html)
        htm += '</div>'
        htm += '</nav></div>'
        return htm


#~ web.elements['header'] = header()
#web.elements['header_filter'] = header_filter()
#~ web.elements['toolbar_filter'] = toolbar_filter()
