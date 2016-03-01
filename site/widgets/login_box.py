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
            if 'google' in self.oauth_enabled:
                htm += '<a title="Login with Google" href="/oauth/google/login"><img src="/static/images/oauth/google.png" /></a>&nbsp;'
            if 'facebook' in self.oauth_enabled:
                htm += '<a title="Login with facebook" class="but row" href="/oauth/facebook/login">Login with Facebook</a>&nbsp;'
            if 'github' in self.oauth_enabled:
                htm += '<a title="Login with twitter" class="but row" href="/oauth/github/login">Login with GitHub</a>'
            htm += '<br /></div>'

        htm += '<p>Or alternatively login with your previously created account.</p>'

        htm+= '''
            <div id="login_box">
            <form id="user_login" method="post" action="/login" ><frameset>
            <label for="username">E-Mail<p><input id="username" name="username" type="text"/></p></label>
            <label for="password">Password<p><input id="password" name="password" type="password"/></p></label>
            <button class="btn" form="user_login" type="submit" value="Login"/>Login</button>
            </frameset></form>
            <a href="/register">Register for an account</a>&nbsp;|&nbsp;<a href="/reset-password">Reset password</a>'''
        htm += '</div>'
        return htm

