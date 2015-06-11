from scaffold.web import www

class control(www.default.html_ui):
    def create(self, appid):
        self.appid = appid
        return self

    def render(self):
        htm = '<a href="https://plus.google.com/hangouts?gid=%s" style="text-decoration:none;">' % self.appid
        htm += '  <img src="https://ssl.gstatic.com/s2/oz/images/stars/hangout/1/gplus-hangout-60x230-normal.png"'
        htm += '    alt="Start a Hangout" style="border:0;width:230px;height:60px;"/>'
        htm += '</a>'
        return htm
