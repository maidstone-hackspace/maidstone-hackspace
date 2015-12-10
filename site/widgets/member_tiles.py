from scaffold.core.widget import base_widget

class control(base_widget):
    """rss feed widgets"""
    def create(self):
        self.data = []
        return self

    def append(self, name, image, description, link, skills):
        self.data.append({
            'name': name,
            'image': image,
            'description': description,
            'link': link,
            'skills': skills})
        return self

    def render(self):
        htm = u''
        count = 0
        for project in self.data:
            htm += u'<div class="tile" style="%s">' % ('clear:left;' if count % 4==0 else '')
            if project.get('image'):
                htm += u'<div class="tile-img" style="background:center no-repeat url(%s);background-size:contain;"></div>' % project.get('image')
            else:
                htm += u'<div class="tile-img"></div>'
            htm += u'<header class="tile-content"><h2><a href="%s/%s">%s</a> Skills in %s</h2></header>' % (
                project.get('link'), project.get('name'), project.get('name'), project.get('skills'))
            htm += u'<div class="tile-content"><p>%s</p></div>' % (project.get('description'))
            htm += u'</div>'
            count += 1
        return htm
