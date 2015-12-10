from flask import session
from flask import request
from flask import Blueprint
from flask import make_response
from flask.ext.login import current_user, login_required
import constants as site

from libs.rss_fetcher import feed_reader
from pages import web
from pages import header, footer
from data import equipment


google_groups_pages = Blueprint('google_group', __name__, template_folder='templates')


@login_required
@google_groups_pages.route("/mailing-list/", methods=['GET'])
def index(request_id=None):
    web.template.create('Maidstone Hackspace - Mailing List')
    header('Mailing List')
    web.page.create('Mailing List')

    
    web.google_groups.create(title='Title', name='maidstone-hackspace')
    web.container.create(web.google_groups.render()).set_classes('margin_default')
    web.page.section(web.container.render())
    
    web.template.body.append(web.page.render())
    return footer()

