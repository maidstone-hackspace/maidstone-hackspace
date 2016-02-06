from scaffold.core.widget import base_widget

class control(base_widget):
    def create(self, title="Join our mailing list"):
        self.title = title
        self.items = []
        return self
    
    def append(self, text):
        self.items.append(text)
        
    
    def render(self):
        htm = '<div id="footer">'
        htm += '<div id="footertop"></div>'
        htm += '<div id="footerbottom"><div class="container">'
        htm += '<div class="copyright">&copy;2016 Maidstone Hackspace</div>'
        htm += ''.join(self.items)
        htm += '</div></div>'
        htm += '<div>'
        return htm
