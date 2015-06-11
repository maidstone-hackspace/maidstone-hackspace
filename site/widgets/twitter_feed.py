from scaffold.web import www

class control(www.default.html_ui):
    """Create the html and javascript for a twitter widget
    https://dev.twitter.com/web/embedded-timelines#customization"""
    script = ["""//twitter code\n!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");\n"""]

    def create(self, username, widget_id):
        self.reset()
        self.username = username
        self.widget_id = widget_id
        return self
    
    def set_size(self, width, height):
        self.width = width
        self.height = height
        return self

    def render(self):
        self.count += 1
        htm = '''
            <div class="twitter-feed">
            <a class="twitter-timeline" href="https://twitter.com/%s" data-widget-id="%s">
            Tweets by @%s
            </a>
            </div>''' % (
            self.username, self.widget_id, self.username)
        return htm
