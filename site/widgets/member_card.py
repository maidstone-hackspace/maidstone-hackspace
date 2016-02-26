from scaffold.core.widget import base_widget_extended

class control(base_widget_extended):

    def create(self, reference, name, active=False):
        super(control, self).create()
        self.reference = reference
        self.name = name
        self.active = active
        return self

    def render(self):
        if self.active is True:
            return '''
            <div id="membercard" class="registered">
                <div class="date">Joined 02/12/2015</div>
                <div class="container">
                    <div class="middle">
                        <p>MHS%s</p><p>%s</p>
                        <a href="/profile/membership/cancel">Cancel Membership</a>
                    </div>
                </div>
            </div>'''  % (self.reference, self.name)
            
        return '''
            <div id="membercard" class="register">
                <form action="/profile/membership" method="post">
                    <fieldset>
                        <legend>Join Maidstone Hackspace</legend>
                        <p><label for="amount">Payment provider<select name="provider"><option value="gocardless">GoCardless</option><option value="paypal">PayPal</option></select></label></p>
                        <p><label for="amount">Subscription Amount<input name="amount" placeholder="20.00" value="20.00" type="text"></label></p>
                        <p class="button"><button type="submit">submit</button></p>
                    </fieldset>
                </form>
            </div>'''

