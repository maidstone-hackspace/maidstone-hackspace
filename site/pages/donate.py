from flask import Blueprint
from flask import request
from flask import redirect, abort

from scaffold import web
from scaffold.core.validate import validate
from pages import header, footer
from data import donate

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
    for item in donate.get_pledges({'environment':int(gocardless_environment=='production')}):
        web.paragraph.create(
            """Currently raised &pound;%.2f towards %s target is &pound;%.2f.""" % (
            item.get('total', 0) if item.get('total', 0) else 0.0,
            item.get('name'), 
            item.get('target', 0)))
        web.page.section(web.paragraph.render())

    web.form.create('Donate to Maidstone Hackspace', '/donate/submit')
    web.form.append(name='reference', label='Reference', placeholder='#lair', value='#lair', input_type='select')
    web.form.append(name='amount', label='Donation Amount', placeholder='50.00', value='50.00')

    web.page.append(web.form.render())
    web.template.body.append(web.page.render())
    return footer()


@donate_pages.route("/donate/populate", methods=['GET'])
def populate_by_name():
    pledge = donate.get_pledge({'name': '#lair'}).get()
    print pledge
    import gocardless
    gocardless.environment = gocardless_environment
    gocardless.set_details(**gocardless_credentials)
    merchant = gocardless.client.merchant()
    for bill in merchant.bills():
        environment = int(gocardless_environment=='production')
        donate.add_payment().execute({'pledge_id': pledge.get('id') , 'reference': bill.id, 'amount': bill.amount_minus_fees, 'environment': environment})
    return abort(404)


@donate_pages.route("/donate/submit", methods=['POST'])
def submit_donation():
    #~ if request.form.get('amount'):
        
        #~ return index()
        
    import gocardless
    gocardless.environment = gocardless_environment
    gocardless.set_details(**gocardless_credentials)
    url = gocardless.client.new_bill_url(
        request.form.get('amount'),
        name=request.form.get('reference'),
        redirect_uri='%s/donate/success' % app_domain)
        #~ redirect_uri='%s/donate/success' % gocardless_redirect_uri if gocardless_redirect_uri else app_domain)
    return redirect(url)


@donate_pages.route("/donate/success", methods=['GET'])
def success_donation():
    # confirm the payment
    
    bill_id = request.args.get('resource_id')
    try:
        import gocardless
        gocardless.environment = gocardless_environment
        gocardless.set_details(**gocardless_credentials)
        gocardless.client.confirm_resource(request.args)
        web.page.create('Thanks for your donation')
        web.paragraph.create(
            """Thanks your payment has been recieved.""")
    except:
        # TODO log what actually has gone wrong
        web.page.create('Something went wrong')
        web.paragraph.create(
            """We could not confirm the payment something may have gone terribly wrong.""")

    if bill_id:
        bill = gocardless.client.bill(bill_id)
        pledge = donate.get_pledge({'name': bill.name}).get()
        
        #~ print dir(bill)

        print bill.amount
        print bill.amount_minus_fees
        print bill.charge_customer_at
        print bill.created_at
        print bill.name
        print bill.payout
        print bill.status
        print bill.user
        environment = int(gocardless_environment=='production')
        donate.add_payment().execute({'pledge_id':pledge.get('id','') , 'reference': bill_id, 'amount': bill.amount_minus_fees, 'environment': environment})


    web.template.create('Maidstone Hackspace')
    header('Maidstone Hackspace Donations')
    web.page.create('Thanks for your donation')
    web.paragraph.create(
        """Thanks your payment has been recieved.""")
    web.page.section(web.paragraph.render())
    web.template.body.append(web.page.render())
    return footer()
