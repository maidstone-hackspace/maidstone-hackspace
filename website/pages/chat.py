from pages import web
from pages import header, footer


def index():
    web.template.create('Maidstone Hackspace - Chat room')
    header('Maidstone Hackspace Chat')
    web.page.create(web.title.create('IRC Chat Room').render())
    web.page.create(web.paragraph.create('Pop in and say hi, please be patient users tend to idle, but will likely respond given a chance.').render())
    web.page.section(web.chat.create('maidstone-hackspace').render())
    web.template.body.append(web.page.set_classes('page col s10 offset-s1').render())
    return footer()
