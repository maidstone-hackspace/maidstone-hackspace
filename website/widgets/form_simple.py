from scaffold.core.widget import base_widget


class control(base_widget):
    method = 'post'
    action = '/'
    inputs = []
    template = '''
        <div class="row">
            <div class="input-field col s12">
              %s
            </div>
          </div>'''

    def create(self, action, method='post'):
        self.action = action
        self.method = method
        return self

    @staticmethod
    def set_template(template):
        if template:
            control.template = template

    def append(self, input_type, input_name, label, values="", classes='validate', disabled='')
        if input_type == 'select' and values:
            if type(values) is not list or tuple:
                self.inputs.append("""<select name="%s" id="%s">%s</select>""" % (input_name, input_name))
                return self
            if len(values[0]) == 2:
                self.inputs.append("""
                    <select name="%s" id="%s">%s</select>""" % (
                        input_name,
                        input_name,
                        "\n".join(["""<option value="%s">%s</option>""" % (value, item) for value, item in values]))
            else:
                self.inputs.append("""
                    <select name="%s" id="%s">%s</select>""" % (
                        input_name,
                        input_name,
                        "\n".join(["""<option value="%s">%s</option>""" % (item, item) for item in values]))
            return self

        self.inputs.append("""
            <input type="%s" name="%s" id="%s" placeholder="%s" %s classes="%s" value="%s" />
            <label for="%s">%s</label>""" % (
                input_type, 
                input_name, 
                input_name, 
                label, 
                'disabled="disabled" ' if disabled else '',
                classes,
                value,
                input_name,
                label)
            )

    def render(self):
        super(control, self).render()
        return """
            <div class="row">
                <form class="col s12" method="%s" action="%s">
                    %s
                </form>
            </div>""" % (
                self.method,
                self.action,
                "\n".join([control.template % input_item for input_item in inputs])
            )
