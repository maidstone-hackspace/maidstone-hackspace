from pages import web
from pages import header, footer
from config.settings import google_captcha, email_server
from libs.mail import sendmail
from flask import get_flashed_messages, flash, request
from libs.recapture import verify_captcha

def contact_page():
    web.template.create('Maidstone Hackspace - Chat room')
    header('Maidstone Hackspace Chat')

    web.contact_form.capture_settings = google_captcha
    web.contact_form.create('Contact Us')
    web.contact_form.enable_capture()
    web.contact_form.render()

    web.simple_form.create()
    web.simple_form.append(input_type='text', input_name='test', label='my label')

    web.page.create(web.title.create('Contact Form').render())
    web.page.section(web.contact_form.render())
    web.template.body.append(web.page.set_classes('page col s10 offset-s1').render())
    return footer()

def submit_contact_page():
    subject = '[%s] - %s' % (
        request.form.get('form_query', 'MHS'),
        request.form.get('form_subject', 'No Subject ?')
    )

    # Check user password the robot check
    print(request.form.get('g-recaptcha-response', ''))
    print(google_captcha.get('secret'))
    print(request.remote_addr)
    success = verify_captcha(
        secret=google_captcha.get('secret'),
        response=request.form.get('g-recaptcha-response', ''),
        remoteip=request.remote_addr)

    if success is False:
        flash('Message failed to send, capture failed to validate are you a robot ?')
        return contact_page()

    # Send Email and let user know if it worked or not
    success = sendmail().send(
            from_address=request.form.get('email'),
            to_address='contact@maidstone-hackspace.org.uk', 
            subject=subject, 
            body=request.form.get('form_message'))

    if success is False:
        flash('Sorry system was unable to send your message, someone has been notified.')
        return contact_page()

    flash('Your message has been sent, we will get back to you shortly.')
    return contact_page()
