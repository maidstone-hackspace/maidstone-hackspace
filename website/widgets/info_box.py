from scaffold.core.widget import base_widget

class control(base_widget):
    """rss feed widgets"""
    def create(self, title=''):
        self.title = title
        self.data = []
        return self

    def append(self, row):
        self.data.append(row)
        return self

    def render(self):
        htm = u'<div class="stats">'
        htm += u'<header class="stats">%s</header>' % self.title
        for project in self.data:
            htm += project
        htm += u'</div>'
        return htm
