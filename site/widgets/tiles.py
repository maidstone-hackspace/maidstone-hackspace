from scaffold.web import www

class control(www.default.html_ui):
    """rss feed widgets"""
    def create(self):
        self.data = []
        return self

    def append(self, title, link, image, description=''):
        self.data.append((title, link, image, description))

    def render(self):
        htm = ''
        for project in self.data:
            htm+='<div class="tile">'
            htm+='<div><img src="%s"/></div>' % project[2]
            htm+='<div><a href="%s">%s</a><p>%s</p></div>' % (project[1], project[0], project[3])
            htm+='</div>'
        return htm
