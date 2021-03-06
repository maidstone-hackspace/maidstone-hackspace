from scaffold.www.default_widgets import page
from flask import get_flashed_messages

class control(page.control):

    def render(self):
        self.count += 1
        self.set_classes('page col s10 offset-s1')
        htm=u"""<div class="row"><div%s>\n""" % self.get_attributes()
        
        # if this is static session will not be available
        try:
            messages = get_flashed_messages()
            if messages:
                htm += u'<ul class="messages">'
                for message in get_flashed_messages():
                    htm += '<li>%s</li>' % message
                htm += '</ul>' 
        except:
            pass
        
        htm+=u"""<header class="pageHeader">\n\t%s</header>\n""" % self.title
        for s in self.sections:
            if s[0]:
                htm+=u"""<section id=\"%s\" class="pageSection col s12">\n\t%s</section>\n""" %(s[0],''.join(s[1]))
            else:
                htm+=u"""<section class="pageSection col s12">\n\t%s</section>\n""" % ''.join(s[1])

        htm+=u"""<footer class="pageFooter col s12">\n\t%s</footer>\n""" % self.foot
        htm+=u"""</div></div>\n"""
        return htm
