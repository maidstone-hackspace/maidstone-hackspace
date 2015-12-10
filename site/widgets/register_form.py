from scaffold.loaders import load_resource
from scaffold.core.widget import base_widget

class control(base_widget):
    html = load_resource('./widgets/register_form.htm')

    def __init__(self):
        self.defaults = {
            'name':'',
            'email':''}
    
    def create(self):
        return self

    def default_values(self, *defaults):
        self.defaults = defaults

    def render(self):
        return self.html.format(**self.defaults)

