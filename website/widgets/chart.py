from scaffold.core.widget import base_widget

class control(base_widget):
    """Create the html and javascript for a twitter widget
    https://dev.twitter.com/web/embedded-timelines#customization"""
    script = ["""//twitter code\n!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");\n"""]

    def create(self, data):
        self.reset()
        return self

    def render(self):
        self.count += 1
        return '<div id="chart"></div>'
