from scaffold.core.widget import base_widget

class control(base_widget):
    link = None
    action = ""
    includes = []
    script = []

    facebook = False
    twitter = True
    plus = True

    plus_script = False
    linkedin_script = False
    facebook_script = False
    twitter_script = False

    size = 'medium'
    annotation = 'inline'

    def create(self, url, plus=None, twitter=None, facebook=None, linkedin=None):
        self.plus = plus
        if plus:
            if self.plus_script is False:
                self.plus_script = True
                self.includes.append('<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>')
        if twitter:
            if self.twitter_script is False:
                self.twitter_script = True
                self.footer.append("""
                    <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>""")
        
        if facebook:
            if self.facebook_script is False:
                self.facebook_script = True
                self.footer.append("""
                    <div id="fb-root"></div><script>(function(d, s, id) {var js, fjs = d.getElementsByTagName(s)[0];if (d.getElementById(id)) return;js = d.createElement(s); js.id = id;js.src = "//connect.facebook.net/en_GB/sdk.js#xfbml=1&version=v2.3";fjs.parentNode.insertBefore(js, fjs);}(document, 'script', 'facebook-jssdk'));</script>""") 
        
        return self

    def url(self, link=None):
        self.link = link
        return self

    def render(self):
        link = ''
        self.count += 1
        htm = ''
        if self.twitter:
            htm += '<a href="https://twitter.com/share" class="twitter-share-button" data-via="%s">Tweet</a>' % self.twitter
        if self.facebook:
            htm += '<div class="fb-like" data-href="%s" data-layout="button_count" data-action="like" data-show-faces="true" data-share="true"></div>' % self.url
        if self.link:
            link = ' data-href="' + self.link + '" '
        if self.plus is True:
            htm += '<div size="standard" class="g-plusone" ' + link + self.action + ' data-size="' + self.size + '" data-annotation="' + self.annotation + '" count="true"></div>'
        return htm

