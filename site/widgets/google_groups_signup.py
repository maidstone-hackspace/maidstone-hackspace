from scaffold.web import www

class control(www.default.html_ui):
    def create(self, title="Join our mailing list", name=''):
        self.title = title
        self.name = name
        return self

    def render(self):
        htm = '<div %s class="google-groups-signup"><h3>Signup %s</h3>' % (self.node_id, self.title)
        htm += '<form class="block" action="http://groups.google.com/group/%s/boxsubscribe">' % self.name
        htm += '<label for="groups-email">Email Address</label>'
        htm += '<input id="groups-email" name="email" class="required"/>'
        htm += '<button type="submit"  />Subscribe</button>'
        htm += '<a href="http://groups.google.com/group/%s">Browse Archives</a>' % self.name
        htm += '</form><div style="clear:both;"></div><div>'
        return htm

#embed in site
#<iframe id="forum_embed"
#  src="javascript:void(0)"
#  scrolling="no"
#  frameborder="0"
#  width="900"
#  height="700">
#</iframe>
#<script type="text/javascript">
#  document.getElementById('forum_embed').src =
#     'https://groups.google.com/forum/embed/?place=forum/maidstone-hackspace'
#     + '&showsearch=true&showpopout=true&showtabs=false'
#     + '&parenturl=' + encodeURIComponent(window.location.href);
#</script> 
