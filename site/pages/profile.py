from flask import Blueprint
from flask import request
from flask import redirect
from flask.ext.login import current_user, login_required

from constants import badge_lookup

from pages import web
from pages import header, footer
from data.site_user import get_user_details, update_membership, update_membership_status, get_user_bio, create_membership
from data.profile import update_description, create_description, fetch_users
from data import badges
from data import members
from config.settings import gocardless_environment, gocardless_credentials
from config.settings import app_domain

from libs.payments import payment
from config.settings import *

#~ import gocardless
#~ gocardless.environment = gocardless_environment
#~ gocardless.set_details(**gocardless_credentials)

profile_pages = Blueprint('profile_pages', __name__, template_folder='templates')



@profile_pages.route("/profile", methods=['GET'])
@login_required
def index():
    web.template.create('Maidstone Hackspace - User profile')
    header('User Profile', url='/profile')
    print current_user
    user = get_user_details({'id': current_user.get_id()}).get()

    name = '%s %s' % (user.get('first_name', '').capitalize(), user.get('last_name', '').capitalize())
    web.page.create('%s - Profile' % name)
    web.columns.create()
    
    web.paragraph.create(
        web.images.create(user.get('profile_image', '/static/images/hackspace.png'), name).add_attributes('width', '200').render()
    )
    web.paragraph.add(name)
    web.paragraph.add('%s' % (user.get('email')))
    web.paragraph.add('Last Login %s' % (user.get('last_login', '')))
    web.paragraph.add('Member since %s' % (user.get('created', '')))
    web.paragraph.add('Description %s' % (user.get('description', '')))
    web.paragraph.add('Skills %s' % (user.get('skills', '')))
    web.columns.append(web.paragraph.render())

    # membership form
    #~ if user.get('status') != 1:
    print user
    web.columns.append(
        web.member_card.create(
            reference=str(user.get('user_id')).zfill(5),
            name=name,
            active=user.get('status')==1
        ).render()
    )

    web.paragraph.create(
        web.link.create(
            'Edit Description',
            'Edit Description',
            '/profile/details'
        ).set_classes('ajaxPopup').render())


    web.columns.append(web.paragraph.render())
    
    web.page.section(web.columns.render())
    web.template.body.append(web.page.render())
    web.template.body.append(web.popup.create('').render())
    
    web.template.body.append('<script type="type/javascript">document.cookie = "status=1";</script>')
    return footer()

@profile_pages.route("/profile/setup", methods=['GET'])
@login_required
def setup():
    """utility url, insert new data and refresh user details"""
    web.template.body.append('Adding badge Types')
    for badge_id, badge_name in badge_lookup.items():
        badges.create_badge().execute({'id': badge_id, 'name': badge_name})

    user_lookup = {}
    for member in fetch_users():
        user_lookup[member.get('email')] = member.get('user_id')

    provider = payment(provider='paypal', style='payment')
    for item in provider.fetch_subscriptions():
        print item

    print user_lookup
    merchant = gocardless.client.merchant()
    #https://jsfiddle.net/api/post/library/pure/
    for paying_member in merchant.subscriptions():
        print dir(paying_member)
        print paying_member.user()
        print paying_member.amount
        user=paying_member.user()
        
        print '---------------'
        print user.email
        user_id = user_lookup.get(user.email)
        print user_id
        update_membership_status().execute({'user_id': user_id, 'status': '1'})
        create_membership().execute({'user_id': user_id, 'status': '1', 'join_date': paying_member.created_at, 'amount': paying_member.amount, 'subscription_id': paying_member.id})


    return footer()

@profile_pages.route("/profile/membership", methods=['POST'])
@login_required
def pay_membership():
    user = get_user_details({'id': current_user.get_id()}).get()
    user_code = str(user.get('user_id')).zfill(5)

    selected_provider = request.form.get('provider', 'gocardless')
    provider = payment(provider=selected_provider, style='payment')
    success_url = '%s/profile/membership/%s/success' % (app_domain, selected_provider)
    failure_url = '%s/profile/membership/%s/failure' % (app_domain, selected_provider)
    url = provider.subscribe(
        amount=request.form.get('amount'),
        name="Membership your membership id is MH%s" % user_code,
        redirect_success=success_url,
        redirect_failure=failure_url
        )


    return redirect(url)


@profile_pages.route("/profile/membership/failure", methods=['GET'])
@profile_pages.route("/profile/membership/cancel", methods=['GET'])
@login_required
def cancel_membership():
    user = get_user_details({'id': current_user.get_id()}).get()
    user_code = str(user.get('user_id')).zfill(5)
    
    subscription = members.fetch_member_subscription({'user_id': current_user.get_id()}).get()
    print subscription.get('provider_id')
    print subscription.get('subscription_reference')
    
    
    provider = payment(provider='paypal', style='payment')
    provider.lookup_provider_by_id(1)
    url = provider.unsubscribe(reference=subscription.get('subscription_reference'))

    members.update_membership_status().execute({'user_id':current_user.get_id(), 'status': '0'})

    return redirect('/profile')

@profile_pages.route("/profile/membership/<provider>/success", methods=['GET'])
@profile_pages.route("/profile/membership/<provider>/success/", methods=['GET'])
@login_required
def membership_signup(provider):
    web.template.create('Maidstone Hackspace')
    header('Maidstone Hackspace Member registration')

    provider = payment(provider=provider, style='payment')

    payment_details = provider.subscribe_confirm(request.args)
    try:
        web.page.create('Thanks for becoming a member.')
        web.paragraph.create(
            """Your membership request has been recieved and will be active shortly.""")
    except:
        # TODO log what actually has gone wrong
        web.page.create('Something went wrong')
        web.paragraph.create(
            """We could not confirm the payment something may have gone terribly wrong.""")

    if payment_details is None:
        return redirect('/profile/membership/failure')

    update_membership_status().execute({'user_id': current_user.get_id(), 'status': '1'})
    #update_membership().execute({'user_id': str(current_user.get_id()), 'status': '1', 'join_date': details.get('start_date'), 'amount': details.get('amount'), 'subscription_reference': details.get('reference')})

    #update_membership_status().execute({'user_id': user_id, 'status': '1'})
    create_membership().execute({
        'user_id': current_user.get_id(), 
        'status': '1', 
        'join_date': payment_details.get('start_date'), 
        'amount': payment_details.get('amount'), 
        'subscription_reference': payment_details.get('reference')})



    web.page.section(web.paragraph.render())
    web.template.body.append(web.page.render())
    return footer()


@profile_pages.route("/profiles/generate", methods=['GET'])
@login_required
def update_profiles():
    """this is used to sync up older accounts"""
    for user in get_users():
        print user

    for payment in get_users():
        print user

    return web.form.render()




@profile_pages.route("/profile/details", methods=['GET'])
@login_required
def edit_profile():
    user_details = get_user_details({'id': current_user.get_id()}).get() or {}
    print user_details
    if not user_details:
        print 'create'
        create_description().execute({'user_id': current_user.get_id()})
    web.form.create('Update your details', '/profile/update')
    web.form.append(name='description', label='Description', placeholder='This is me i am great', value=user_details.get('description') or '')
    web.form.append(name='skills', label='skills', placeholder='python, arduino, knitting', value=user_details.get('skills') or '')
    return web.form.render()


@profile_pages.route("/profile/update", methods=['POST'])
@login_required
def update_profile():
    """ handle form submit to update description and skills"""
    data = {
        'user_id': current_user.get_id(),
        'skills': request.form.get('skills'),
        'description': request.form.get('description')}
    user_details = get_user_details({'id': current_user.get_id()}).get() or {}
    if user_details.get('user_detail_id', None) is None:
        create_description().execute(data)
    else:
        update_description().execute(data)
    return redirect('/profile')
