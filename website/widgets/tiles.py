from scaffold.core.widget import base_widget

class control(base_widget):
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
        return self

    def render(self):
        htm = u'<div class="col s12">'
        for project in self.data:
            htm += u'<div class="tile col s4"><div class="tile-border card">'
            if project.get('image'):
                #~ htm += u'<div class="tile-img" style="%s"><img src="%s"/></div>' % (background, project.get('image'))
                htm += u'<div class="tile-img" style="background:center no-repeat url(%s);background-size:contain;"></div>' % project.get('image')
            else:
                htm += u'<div class="tile-img"></div>'
            htm += u'<header class="tile-header"><h2><a href="%s">%s</a> <br />By %s</h2></header>' % (
                project.get('link'), project.get('title'), project.get('author'))
            htm += u'<div class="card-content content"><p>%s</p></div>' % (project.get('description'))
            htm += u'</div></div>'
        htm += u'</div>'
        return htm
