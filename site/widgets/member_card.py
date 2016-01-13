from scaffold.core.widget import base_widget_extended

class control(base_widget_extended):

    def create(self, reference, name):
        super(control, self).create()
        self.reference = reference
        self.name = name
        return self

    def render(self):
        
        content = '''
            <div class="date">Joined 02/12/2015</div>
            <div class="container">
                <div class="middle">
                    <p>MHS%s</p><p>%s</p>
                </div>
            </div>'''  % (self.reference, self.name)
        content='<form action="/profile/membership" method="post"><fieldset><legend>Join Maidstone Hackspace</legend><p><label for="amount">Subscription Amount<input name="amount" placeholder="20.00" value="20.00" type="text"></label></p><p class="button"><button type="submit">submit</button></p></fieldset></form>'
        return '''
            <div id="membercard">
                %s
            </div>''' % content
