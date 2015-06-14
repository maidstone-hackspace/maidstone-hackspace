from scaffold.web import www

class control(www.default.html_ui):
    """rss feed widgets"""
    def create(self):
        self.data = []
        return self

    def append(self, title, author, date, link, image, description=''):
        self.data.append({
        'title': title, 
        'author': author,
        'date': date,
        'link': link,
        'image': image, 
        'description': description})

    def render(self):
        htm = u''
        for project in self.data:
            htm += u'<div class="tile">'
            if project.get('image'):
                htm += u'<div class="tile-img"><img src="%s"/></div>' % project.get('image')
            else:
                htm += u'<div class="tile-img"></div>'
            htm += u'<header class="tile-content"><h2><a href="%s">%s</a> By %s</h2></header>' % (
                project.get('link'), project.get('title'),project.get('author'))
            htm += u'<div class="tile-content"><p>%s</p></div>' % (project.get('description'))
            htm += u'</div>'
        return htm
