from scaffold.core.widget import base_widget

class control(base_widget): 
    
    def create(self, title, url, method='post', enctype="", button='submit'):
        self.title = title
        self.url = url
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
                
            htm+='<p><label for="%s">%s<input type="%s" name="%s" placeholder="%s" value="%s"></label></p>' % (name, label, input_type ,name, placeholder, value)
        htm+='<button type="submit">%s</button>' % self.button
        htm+='</fieldset></form>'
        return htm
