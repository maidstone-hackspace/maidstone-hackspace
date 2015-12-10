from scaffold.core.widget import base_widget_extended

class control(base_widget_extended):

    def create(self, title="Join our mailing list", name=''):
        super(control, self).create()
        self.title = title
        self.name = name
        return self

    def render(self):
        self.script.append(
            """document.getElementById("forum_embed").src = "https://groups.google.com/forum/embed/?place=forum/%s" + "&showsearch=true&showpopout=true&parenturl=" + encodeURIComponent(window.location.href);""" % self.name)
        return '<iframe id="forum_embed" src="javascript:void(0)" style="background-color:#fff;width:100%;" scrolling="no" frameborder="0" width="900" height="700"></iframe>'


#~ <iframe id="forum_embed"
  #~ src="javascript:void(0)"
  #~ scrolling="no"
  #~ frameborder="0"
  #~ width="900"
  #~ height="700">
#~ </iframe>
#~ <script type="text/javascript">
  #~ document.getElementById('forum_embed').src =
     #~ 'https://groups.google.com/forum/embed/?place=forum/maidstone-hackspace'
     #~ + '&showsearch=true&showpopout=true&showtabs=false'
     #~ + '&parenturl=' + encodeURIComponent(window.location.href);
#~ </script> 


#~ <html><body>
#~ <iframe id="forum_embed" src="javascript:void(0)"
  #~ scrolling="no" frameborder="0"  width="746" height="1200">
#~ </iframe>
#~ <script type="text/javascript">
  #~ document.getElementById('forum_embed').src =
     #~ "https://groups.google.com/forum/embed/?place=forum/sbml-discuss"
     #~ + "&parenturl=" + encodeURIComponent(window.location.href);
#~ </script>
#~ </body></html>
