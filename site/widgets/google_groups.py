from scaffold.web import www

class control(www.default.html_ui):

    def create(self, title="Join our mailing list", name=''):
        self.title = title
        self.name = name
        return self

    def render(self):
        self.script.append(
            """document.getElementById("forum_embed").src = "https://groups.google.com/forum/embed/?place=forum/%s" + "&showsearch=true&showpopout=true&parenturl=" + encodeURIComponent(window.location.href);""" % self.name)
        return '<iframe id="forum_embed" src="javascript:void(0)" scrolling="no" frameborder="0" width="900" height="700"></iframe>'
