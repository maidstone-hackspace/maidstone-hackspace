from flask import session
from flask import request
from flask.ext.login import current_user, login_required
import constants as site

from libs.rss_fetcher import feed_reader
from pages import web
from pages import header, footer
from data import members


@login_required
def index():
    web.template.create('Maidstone Hackspace - Members')
    header('Members')
    web.page.create('Members')
    web.member_tiles.create()
    for item in members.get_members():
        print item
        name = '%s %s' % (item.get('first_name'), item.get('last_name'))
        user_id = '%s %s' % (item.get('first_name'), item.get('last_name'))
        web.member_tiles.append(
            name = name, 
            image = item.get('profile_image'), 
            description=item.get('description') or 'Reclusive raccoon', 
            link=item.get('user_id'),
            skills=item.get('skills') or 'badger taunting')
    web.container.create(web.member_tiles.render()).set_classes('members')
    web.page.section(web.container.render())
    web.template.body.append(web.page.render())

    return footer()

@login_required
def profile(user_id, user_name):
    web.template.create('Maidstone Hackspace - User profile')
    header('User Profile')
    user = members.get_member_profile({'id': user_id}).get()
    web.page.create('')

    name = '%s %s' % (user.get('first_name', ''), user.get('last_name', ''))
    
    web.paragraph.create(
        web.images.create(user.get('profile_image', '/static/images/hackspace.png'), name).add_attributes('width', '200').render()
    )
    web.paragraph.add(name)
    web.paragraph.add('%s' % (user.get('email')))
    web.paragraph.add('Last Login %s' % (user.get('last_login', '')))
    web.paragraph.add('Member since %s' % (user.get('created', '')))

    web.page.section(web.paragraph.render())
    web.template.body.append(web.page.render())

    return footer()
