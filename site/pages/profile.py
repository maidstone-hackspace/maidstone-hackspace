from flask import Blueprint
from flask import request
from flask import redirect
from flask.ext.login import current_user, login_required
import gocardless

from pages import web
from pages import header, footer
from data.site_user import get_user_details, update_membership_status, get_user_bio
from data.profile import update_description, create_description
from config.settings import gocardless_environment, gocardless_credentials
from config.settings import app_domain

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


@profile_pages.route("/profile/membership", methods=['POST'])
@login_required
def pay_membership():
    import gocardless
    
    user = get_user_details({'id': current_user.get_id()}).get()
    user_code = str(user.get('user_id')).zfill(5)
    
    gocardless.environment = gocardless_environment
    gocardless.set_details(**gocardless_credentials)
    url = gocardless.client.new_subscription_url(
        amount=request.form.get('amount'), 
        interval_length=1, 
        interval_unit="month",
        name="Membership your membership id is MH%s" % user_code,
        redirect_uri='%s/profile/gocardless' % app_domain)
    return redirect(url)


@profile_pages.route("/profile/membership/cancel", methods=['GET'])
@login_required
def cancel_membership():
    import gocardless
    
    user = get_user_details({'id': current_user.get_id()}).get()
    user_code = str(user.get('user_id')).zfill(5)
    
    gocardless.environment = gocardless_environment
    gocardless.set_details(**gocardless_credentials)

    subscription = gocardless.client.subscription('0540QD22SKND')
    subscription.cancel()
    return redirect(url)


@profile_pages.route("/profile/gocardless", methods=['GET'])
@login_required
def gocardless_signup():
    web.template.create('Maidstone Hackspace')
    header('Maidstone Hackspace Member registration')

    # confirm the payment
    bill_id = request.args.get('resource_id')
    try:
        import gocardless
        gocardless.environment = gocardless_environment
        gocardless.set_details(**gocardless_credentials)
        print gocardless.client.confirm_resource(request.args)
        web.page.create('Thanks for becoming a member.')
        web.paragraph.create(
            """Your membership request has been recieved and will be active shortly.""")
    except:
        # TODO log what actually has gone wrong
        web.page.create('Something went wrong')
        web.paragraph.create(
            """We could not confirm the payment something may have gone terribly wrong.""")

    update_membership_status().execute({'user_id': current_user.get_id(), 'status': '1'})
    update_membership().execute({'user_id': current_user.get_id(), 'status': '1', 'join_date': '', 'amount': '', 'subscription_id': ''})

    web.page.section(web.paragraph.render())
    web.template.body.append(web.page.render())
    return footer()



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
