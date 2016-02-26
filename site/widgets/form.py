from scaffold.core.widget import base_widget

class control(base_widget): 
    
    def create(self, title, url, method='post', enctype="", button='submit', seperator=','):
        self.title = title
        self.url = url
        self.seperator = seperator
        self.method = method
        self.button = button
        self.enctype = enctype
        self.content = []
        return self

    def append(self, label, name, placeholder='', value='', input_type='text'):
        self.content.append((label, name, value, placeholder, input_type))
        return self


    def render(self):
        htm='<form action="%s" method="%s" ><fieldset>' % (self.url, self.method)
        if self.title:
            htm += '<legend>%s</legend>' % self.title
        for label, name, value, placeholder, input_type in self.content:
            if input_type == 'hidden':
                htm+='<input type="hidden" name="%s" value="%s">' % (name, value)
                continue
            if input_type == 'select':
                htm += '<p><label for="%s">%s<select name="%s">' % (name, label, name)
                for item in placeholder.split(self.seperator):
                    htm += '<option value="%s" %s>%s</option>' % (
                        item, 
                        'selected="selected"' if item==value else '',
                        item)
                htm += '</select></label></p>'
                continue
            checked = ''
            if input_type == 'radio':
                if placeholder == value:
                    checked = ' checked="checked"'
                
            htm+='<p><label for="%s">%s<input type="%s" name="%s" placeholder="%s" value="%s"%s></label></p>' % (name, label, input_type ,name, placeholder, value, checked)
        htm+='<p class="bottom full_width"><button type="submit">%s</button></p>' % self.button
        htm+='</fieldset></form>'
        return htm
