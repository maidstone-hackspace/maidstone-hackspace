from scaffold.core.widget import base_widget

class control(base_widget):
    link = None
    includes = ['<script src="https://www.google.com/recaptcha/api.js"></script>']
    site_key = None

    def create(self, url):
        self.url = url
        self.footer.append("""
            <script src='https://www.google.com/recaptcha/api.js'></script>""") 

    def render(self):
        self.count += 1
        if self.site_key:
            return '''<div class="g-recaptcha" data-sitekey="%s"></div>''' % (self.site_key)
        return 'Missing key, captcha unavailable'

