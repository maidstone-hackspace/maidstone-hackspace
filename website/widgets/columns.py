from scaffold.core.widget import base_widget

class control(base_widget):

    def create(self, cols=2):
        self.cols = []
        self.current_column = 0
        for c in range(0, cols):
            self.cols.append([])
        return self

    def next_column(self):
        for c in self.cols:
            yield ''.join(c)

    def append(self, content):
        if self.current_column > len(self.cols)-1:
            self.current_column = 0
        self.cols[self.current_column].append(content)
        self.current_column += 1
        return self

    def render(self):
        return '<div class="col">%s</div><div style="clear:left;"></div>' % '</div><div class="col">'.join(self.next_column())
