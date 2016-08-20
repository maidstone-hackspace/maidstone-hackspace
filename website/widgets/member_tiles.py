from scaffold.core.widget import base_widget_extended

class control(base_widget_extended):
    """rss feed widgets"""
    def create(self):
        self.data = []
        return self

    def append(self, name, image, description, link, badges, skills):
        self.data.append({
            'name': name,
            'image': image,
            'description': description,
            'link': link,
            'badges': badges,
            'skills': skills})
        return self

    def render(self):
        htm = u''
        count = 0
        for project in self.data:
            htm += u'<div class="tile col s3" style="%s">' % ('clear:left;' if count % 4==0 else '')
            if project.get('image'):
                htm += u'<div class="tile-img" style="background:center no-repeat url(%s);background-size:contain;"></div>' % project.get('image')
            else:
                htm += u'<div class="tile-img"></div>'
            htm += u'<header class="tile-content"><h2><a href="%s/%s">%s</a> Skilled in %s' % (
                project.get('link'), project.get('name'), project.get('name'), project.get('skills'))
            for badge in project.get('badges'):
                htm += u'<img class="badge" title="%s" src="/static/images/badges/%s.png" />' % (badge.capitalize(), badge)
            htm += '</h2></header>'
            htm += u'<div class="tile-content"><p>%s</p></div>' % (project.get('description'))
            htm += u'</div>'
            count += 1
        return htm
