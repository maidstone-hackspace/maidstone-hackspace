from flask import Blueprint
from flask.ext.login import login_required

from pages import web
from pages import header, footer

google_groups_pages = Blueprint('google_group', __name__, template_folder='templates')


@login_required
@google_groups_pages.route("/mailing-list/", methods=['GET'])
def index(request_id=None):
    web.template.create('Maidstone Hackspace - Mailing List')
    header('Mailing List')
    web.page.create('Mailing List')

    web.page.section(web.link.create(title='View google group', content='View google group', link='https://groups.google.com/forum/#!forum/maidstone-hackspace').render())
    web.google_groups.create(title='Title', name='maidstone-hackspace')
    web.container.create(web.google_groups.render()).set_classes('margin_default')
    web.page.append(web.container.render())

    web.template.body.append(web.page.set_classes('page col s10 offset-s1').render())
    return footer()

