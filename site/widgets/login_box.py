from scaffold.core.widget import base_widget

class control(base_widget):
    oauth_enabled = set()

    def create(self):
        return self

    def enable_oauth(self, name):
        self.oauth_enabled.add(name)
        return self

    def render(self):
        htm = '<div id="login_box">'

        htm += '<p>Please login with one of the oauth provider below, which is more secure and does not store passwords on our system.</p>'
        if self.oauth_enabled:
            htm += '<div class="providers">'
            
            htm += '<a title="Login with Google" href="/oauth/google"><img src="/static/images/oauth/google.png" /></a><br />'
            #htm += '<a title="Login with facebook" href="/oauth/github">Facebook</a>.<br />'
            #htm += '<a title="Login with twitter" href="/oauth/teitter">Twitter</a>.<br />'
            htm += '</div>'

        htm += '<p>Or alternatively login with your previously created account.</p>'

        htm+= '''
            <div id="login_box">
            <form id="user_info" method="post" action="/login" ><frameset>
            <label for="username">E-Mail<p><input id="username" name="username" type="text"/></p></label>
            <label for="password">Password<p><input id="password" name="password" type="password"/></p></label>
            <input class="btn" type="submit" value="Login"/>
            </frameset></form>
            <a href="/register">Register for an account</a>&nbsp;|&nbsp;<a href="/reset-password">Reset password</a>'''



        htm += '</div>'



        return htm

