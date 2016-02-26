from flask.ext.login import login_required

from pages import web
from pages import header, footer
from data import members
from data import badges
from constants import badge_lookup

b = {'1':'test', '2': 'abc'}

@login_required
def index():
    web.template.create('Maidstone Hackspace - Members')
    header('Members')
    web.page.create('Members')
    web.member_tiles.create()

    members_badges = badges.fetch_user_badges_grouped()
    count_users = 0
    count_members = 0
    for item in members.get_members():
        member_badges = [
            badge_lookup.get(b, '') 
            for b in members_badges.get(item.get('user_id'), [])]

        name = '%s %s' % (item.get('first_name'), item.get('last_name'))
        web.member_tiles.append(
            name = name, 
            image = item.get('profile_image'), 
            description=item.get('description') or 'Reclusive raccoon', 
            link=item.get('user_id'),
            badges=member_badges,
            skills=item.get('skills') or 'badger taunting')
        count_users += 1
        if item.get('status') is 1:
            count_members += 1
    print count_members
    web.page.section('Members %d' % count_members)
    web.page.section('Users %d' % count_users)
    
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
    
    #~ web.paragraph.add('%s' % (user.get('email')))
    web.paragraph.add('Last Login %s' % (user.get('last_login', '')))
    web.paragraph.add('Member since %s' % (user.get('created', '')))
    
    web.list.create('badges', 'ul')
    web.list.append(web.images.create('/static/images/badges/member.png').render())
    web.list.append(web.images.create('/static/images/badges/member.png').render())
    web.list.append(web.images.create('/static/images/badges/member.png').render())
    
    web.paragraph.add(web.list.render())

    web.page.section(web.paragraph.render())
    web.template.body.append(web.page.render())

    return footer()
