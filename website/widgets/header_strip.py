from scaffold.core.widget import base_widget

class control(base_widget):
    script = ["""
        $(document).ready(function(){
            $('#mini_logo').on("click", function(e){
                e.preventDefault();
                $('#member_navigation').toggle();
            });
        });
        """]
            
    def create(self, params):
        super(control, self).create()
        self.params = params
        self.social_html = []
        return self

    def social(self, htm):
        self.social_html.append(htm)

    def render(self):
        url = '/login'
        if self.params.get('logged_in'):
            url = '/profile'
        htm = '<div id="headerstrip"><nav class="navstrip">'
        htm += '<div class="left"><a id="mini_logo" href="%s"><img src="%s/static/images/hackspace.png" class="mini-logo"></a><span class="mini-logo-text">Maidstone Hackspace</span></div>' % (url, self.uri.rel)
        htm += '<div class="social">'
        htm += "".join(self.social_html)
        htm += '</div>'
        htm += '</nav></div>'
        return htm


#~ web.elements['header'] = header()
#web.elements['header_filter'] = header_filter()
#~ web.elements['toolbar_filter'] = toolbar_filter()
