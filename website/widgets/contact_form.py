import requests
from scaffold.core.widget import base_widget_extended
from libs.recapture import verify_captcha
#~ from widgets import recaptcha


class control(base_widget_extended):
    includes = ['<script src="https://www.google.com/recaptcha/api.js"></script>']
    capture_url = 'https://www.google.com/recaptcha/api/siteverify'
    #~ capture_settings = {
        #~ 'method': 'get_html',
        #~ 'app_id': '242787',
        #~ 'app_key': '3be3d6d48255e43b750e4865ba9e8827',
        #~ 'is_auto_submit': '0',
        #~ 'platform': 'api'
    #~ }

    capture_settings = {
        'secret': '',
        'response': '',
        'remoteip': ''
    }

    def create(self, title='', capture=False):
        super(control, self).create()
        self.title = title
        self.data = []
        self.capture_html = ''
        return self

    def enable_capture(self, capture_settings=None):
        if capture_settings:
            pass
        #~ response = requests.post(self.capture_url, data=self.capture_settings)
        #~ import base64
        #~ print(response.decode('utf-8'))
        #~ print(base64.b64encode(response.content))
        #~ print(base64.b64encode(response.content))
        #~ print(response.content.encode('utf-8'))
        
        self.capture_html = """
            <div class="row">
                <div class="input-field col s12">
                    <div class="g-recaptcha" data-sitekey="%s"></div> 
                </div>
            </div>""" % (self.capture_settings.get('site', ''))

    def append(self, row):
        self.data.append(row)
        return self

    def render(self):
        super(control, self).render()
        return """
        <div class="row">
            <form class="col s12" action="/contact-us/" method="post">
            <div class="row">
                <div class="input-field col s6">
                <input id="name" type="text" name="name" class="validate">
                <label for="name">Your Name</label>
                </div>
            </div>
            <div class="row">
                <div class="input-field col s12">
                <input id="email" type="email" name="email" class="validate">
                <label for="email">Your e-mail</label>
                </div>
            </div>
            <div class="row">
                <div class="input-field col s12">
                <input id="subject" type="text" name="form_subject" class="validate">
                <label for="subject">Subject</label>
                </div>
            </div>
            <div class="row">
                <div class="input-field col s12">
                    <textarea id="form_message" name="form_message" class="materialize-textarea"></textarea>
                    <label for="form_message">Message</label>
                </div>
            </div>
            <div class="row">
                <div class="input-field col s12">
                    <select id="form_query" name="form_query">
                        <option value="General">General</option>
                        <option value="Donate">Donate equipment money or time</option>
                        <option value="Event">Event</option>
                    </select>
                    <label for="form_query">Equiry type</label>
                </div>
            </div>
            %s
            <div class="row">
                <div class="input-field col s12">
                    <button type="submit">Send</button>
                </div>
            </div>
            
            </form>
        </div>""" % (self.capture_html)

#sweet captcha
#~ Application ID:242787
#~ Application Key: 3be3d6d48255e43b750e4865ba9e8827
#~ Application Secret: 3295baa3645fb2c2670fdb8990023664
#~ import requests

#~ values = {
    #~ 'method': 'get_html',
    #~ 'app_id': '242787',
    #~ 'app_key': '3be3d6d48255e43b750e4865ba9e8827',
    #~ 'is_auto_submit': '0',
    #~ 'platform': 'api'
#~ }

#~ values = {
    #~ 'method': 'get_html',
    #~ 'app_id': '242787',
    #~ 'app_key': '3be3d6d48255e43b750e4865ba9e8827',
    #~ 'sckey': 'from the form',
    #~ 'scvalue': 'from the form',
    #~ 'platform': 'api'
#~ }

#~ requests.post('http://www.sweetcaptcha.com/api', data=values)

