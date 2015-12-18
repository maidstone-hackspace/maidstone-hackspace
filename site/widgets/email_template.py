import os
from scaffold.readers.markdown_reader import markdown_reader
from scaffold.core.widget import base_widget

class control(base_widget):
    filepath = ''

    def create(self, filepath):
        self.filepath = filepath
        return self

    def render(self):
        print os.path.abspath(self.filepath)
        return markdown_reader(
            os.path.abspath(self.filepath)
        ).render()
