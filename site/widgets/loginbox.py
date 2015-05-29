from scaffold.web import web
from scaffold.web import www

class login_box(www.default.html_ui):
    def create(self):
        #self.params = params
        return self

    def render(self):
        htm = '<img id="login_img" src="/static/template/images/mantis-shrimp.png" />'
        htm += '<div id="login_box">Use Mantis Login'
        htm += '<form id="user_info" method="post" action="/login" >'
        htm += '<label>username</label><input id="username" name="username"/>'
        htm += '<label>password</label><input id="password" name="password" type="password"/>'
        htm += '<input type="submit" value="Login"/>'
        htm += '</form>'
        htm += '</div>'
        return htm

def render(html):
    response = make_response(html)
    if request.args.get('dbselect'):
        db = request.args.get('dbselect')
        response.set_cookie('db', db)
    return response
