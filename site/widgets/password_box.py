from scaffold.core.widget import base_widget

class control(base_widget):
    oauth_enabled = False
    
    def create(self, message='', reset=False):
        self.message = message
        self.reset = reset
        return self

    def render(self):
        if self.reset is True:
            return '''
                <div id="login_box">
                <form id="user_info" method="post" action="/reset-password" >
                <label>E-Mail</label><input id="email" name="email" type="test"/>
                <input type="Submit" value="Send reset instructions"/>
                </form>'''

        return '''
            <div id="login_box">
            <form id="user_info" method="post" action="/change-password" >
            <label>Old password</label><input id="password" name="password_old" type="password"/>
            <label>New Password</label><input id="password" name="password_new" type="password"/>
            <label>Confirm Password</label><input id="password" name="password_confirm" type="password"/>
            <input type="Update" value="password_change"/>
            </form>'''
        return htm

