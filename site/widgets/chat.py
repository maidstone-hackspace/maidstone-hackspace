from scaffold.core.widget import base_widget

class control(base_widget):

    def create(self, channel):
        self.channel = channel
        return self

    def render(self):
        self.count += 1
        return """<div class="social-chat"><div class="contain"><iframe src="http://webchat.freenode.net?channels=%%23%s&uio=MTE9MjU207"></iframe></div></div>""" % self.channel
