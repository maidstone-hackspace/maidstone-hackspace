from flask import Blueprint
from flask import request
from flask import redirect, abort

from scaffold import web
from scaffold.core.validate import validate
from pages import header, footer
from data import donate, site_user, badges, members

from libs.payments import payment
from config.settings import *

donate_pages = Blueprint('donate_pages', __name__, template_folder='templates')

@donate_pages.route("/donate", methods=['GET'])
@donate_pages.route("/donate/", methods=['GET'])
def index():
    web.template.create('Maidstone Hackspace')
    header('Maidstone Hackspace Donations')
    web.page.create('Make a donation')

    web.paragraph.create(
        """If you would like to donate to the space please type an amount and use the reference code for what ever your donating for, for example use #lair to donate to getting a space.
        We may run pledges in the future for equipment in which case use the reference for the equipment your pledging towards.""")

    web.page.section(web.paragraph.render())
    #~ for item in donate.get_pledges({'environment':int(gocardless_environment=='production')}):
        #~ web.paragraph.create(
            #~ """Currently raised &pound;%.2f towards %s target is &pound;%.2f.""" % (
            #~ item.get('total', 0) if item.get('total', 0) else 0.0,
            #~ item.get('name'), 
            #~ item.get('target', 0)))
        #~ web.page.section(web.paragraph.render())


    web.form.create('Donate to Maidstone Hackspace', '/donate/submit')
    web.form.append(name='provider', label='GoCardless', placeholder='gocardless', value='gocardless', input_type='radio')
    web.form.append(name='provider', label='PayPal', placeholder='', value='paypal', input_type='radio')
    web.form.append(name='reference', label='Reference', placeholder='#lair', value='#lair', input_type='select')
    web.form.append(name='amount', label='Donation Amount', placeholder='50.00', value='50.00')
    web.page.append(web.form.render())
    
    web.template.body.append(web.page.render())
    return web.render()


@donate_pages.route("/donate/populate", methods=['GET'])
def populate_by_name():
    web.template.create('Maidstone Hackspace')
    header('Maidstone Hackspace Donations')

    pledge = donate.get_pledge({'name': '#lair'}).get()

    import gocardless
    gocardless.environment = gocardless_environment
    gocardless.set_details(**gocardless_credentials)
    merchant = gocardless.client.merchant()

    web.template.body.append('Adding Badges')
    badges.create_badge().execute({'name': 'member'})
    badges.create_badge().execute({'name': 'backer'})
    badges.create_badge().execute({'name': 'teacher'})
    badges.create_badge().execute({'name': 'chairman'})
    badges.create_badge().execute({'name': 'treasurer'})
    badges.create_badge().execute({'name': 'secretary'})

    web.template.body.append('Populating users')
    user_list = {}
    #make sure we have all users in the system
    print '--------------'
    #~ users_emails = []
    for user in merchant.users():
        #~ print dir(user)
        user_list[user.id] = user.email
        #~ users_emails.append(user.email)
        site_user.create_basic_user().execute({
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        })

    #get the users ids and emails 
    #~ users = {}
    #~ for member in members.get_members():
        #~ for key, value in user_list.items():
            #~ if value == member.get('email'):
                #~ user_list[key] = member.get('user_id')

    badge_lookup = {badge.get('name'):badge.get('id') for badge in badges.fetch_badges()}

    web.template.body.append('Setting Donation Badges')
    environment = int(gocardless_environment=='production')
    for bill in merchant.bills():
        web.template.body.append(str(bill))

        matched_user = None
        for user_id, user_email in user_list.items():
            if user_email == user.email:
                matched_user = user_id

        donate.add_payment().execute({'user_id': matched_user,'pledge_id': pledge.get('id') , 'reference': bill.id, 'amount': bill.amount_minus_fees, 'environment': environment})

        if matched_user:
            badges.assign_badge().execute({'badge_id': badge_lookup.get('backer'), 'user_id': matched_user})

    return web.render()


@donate_pages.route("/donate/submit", methods=['POST'])
def submit_donation():
    provider = payment(
        provider='paypal',
        style='payment')
    
    # convert donation amount to 2 decimal places, paypal seems to require this else it errors
    donation_amount = '{0:.2f}'.format(float(request.form.get('amount')))
    url = provider.make_donation(
        amount=donation_amount,
        reference=request.form.get('reference', ''),
        redirect_success='%s/donate/success' % app_domain,
        redirect_failure='%s/donate/failure' % app_domain
        )

    return redirect(url)


@donate_pages.route("/donate/success", methods=['GET'])
def donation_successfull():

    provider = payment(
        provider='paypal',
        style='payment')

    bill = provider.confirm(request.args)
    if bill:
        pledge = donate.get_pledge({'name': bill.get('name')}).get()

        environment = int(provider.environment=='production')
        donate.add_payment().execute({
            'provider_id': provider.provider_id, 
            'pledge_id': pledge.get('id',''), 
            'reference': bill.get('reference'), 
            'amount': bill.get('amount'), 
            'environment': environment})
        
        web.page.create('Thanks for your donation')
        web.paragraph.create(
            """Thanks your payment has been recieved.""")
    else:
        web.page.create('Something went wrong')
        web.paragraph.create(
            """We could not confirm the payment something may have gone terribly wrong.""")

    web.template.create('Maidstone Hackspace')
    header('Maidstone Hackspace Donations')
    web.page.create('Thanks for your donation')
    web.paragraph.create(
        """Thanks your payment has been recieved.""")
    web.page.section(web.paragraph.render())
    web.template.body.append(web.page.render())
    return web.render()




@donate_pages.route("/donate/failure", methods=['GET'])
def donation_failed():
    web.template.create('Maidstone Hackspace')
    header('Maidstone Hackspace Donations')
    web.page.create('Looks like something went wrong.')
    web.paragraph.create(
        """Sorry looks like something went wrong while trying to take this payment.""")
    web.page.section(web.paragraph.render())
    web.template.body.append(web.page.render())
    return web.render()
