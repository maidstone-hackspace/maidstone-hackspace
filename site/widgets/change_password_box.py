from scaffold.core.widget import base_widget

class control(base_widget):
    oauth_enabled = False
    url = '/change-password'
    
    def create(self, message='', reset=False):
        self.message = message
        self.reset = reset
        return self

    def render(self):
        return '''
            <div id="login_box">
            <form id="user_info" method="post" action="/change-password" >
            <label>Password</label><input id="password" name="password" type="password"/>
            <label>Password Confirm</label><input id="password" name="password_confirm" type="password"/>
            <input type="Submit" value="Update"/>
            </form>'''
