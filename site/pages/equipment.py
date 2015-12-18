from flask import request
from flask import Blueprint
from flask import make_response
from flask.ext.login import current_user, login_required

from pages import web
from pages import header, footer
from data import equipment


equipment_pages = Blueprint('equipment_pages', __name__, template_folder='templates')



@equipment_pages.route("/equipment/add/", methods=['GET'])
@equipment_pages.route("/equipment/edit/<request_id>/", methods=['GET'])
@login_required
def equipment_view(request_id=None):
    """home page"""
    equipment_data = request.form
    if request_id:
        equipment_data = equipment.get_request({'id': request_id}).get()

    web.form.create('Equipment wish list', '/equipment')
    web.form.append(name='id', label='', placeholder='', value=equipment_data.get('id') or '', input_type='hidden')
    web.form.append(name='name', label='name', placeholder='Screws 3.5 x 20mm', value=equipment_data.get('name') or '')
    web.form.append(name='url', label='url', placeholder='Link to example', value=equipment_data.get('url') or '')
    web.form.append(name='description', label='description', placeholder='Notes / Description', value=equipment_data.get('description') or '')
    web.form.append(name='price', label='price', placeholder='10.00', value=equipment_data.get('price') or '')    
    return make_response(web.form.render())



@equipment_pages.route("/equipment", methods=['POST'])
@login_required
def equipment_submit():
    insert()
    return make_response(index())


@equipment_pages.route("/equipment/delete/<request_id>", methods=['GET'])
@login_required
def equipment_delete(request_id):
    #~ delete()
    return make_response(index())


def insert():
    data = {}
    data['id'] = request.form.get('id')
    data['name'] = request.form.get('name')
    data['user_id'] = current_user.get_id()
    data['price'] = request.form.get('price')
    data['url'] = request.form.get('url')
    data['description'] = request.form.get('description')
    if data['id']:
        equipment.update().execute(data)
    else:
        equipment.create().execute(data)

@equipment_pages.route("/equipment", methods=['GET'])
@login_required
def index(request_id=None):
    web.template.create('Maidstone Hackspace - Equipment')
    header('User Profile')
    web.page.create('Equipment wish list')
    web.list.create()
    for item in equipment.get_requests():
        if item.get('name'):
            values = []
            if item.get('url'):
                values.append(
                    web.link.create(item.get('name'), item.get('name'), item.get('url')).render()
                )
            else:
                values.append(item.get('name'))
            

            if item.get('price'):
                values.append( '&pound;' + str(item.get('price')))
            if item.get('user_id') == current_user.get_id():
                values.append(
                    web.link.create('edit', 'edit', '/equipment/edit/%s' % item.get('id')).set_classes('ajaxPopup').render())
            
            if item.get('description'):
                web.list.append(' - '.join(values) + web.paragraph.create(item.get('description')).render())
            else:
                web.list.append(' - '.join(values))
    
    web.paragraph.create('''This is wanted list, if you can donate any of these items great,
        if not we will look at running pledges or using hackspace funds to get these items where appropriate.''')
    
    web.page.section(web.paragraph.render())
    web.page.section(web.list.render())
    web.template.body.append(web.page.render())

    web.template.body.append(
        web.action_bar.create(
            url='/equipment/add',
            title='Add equipment', 
            node_id='add-equipment',
            classes='ajaxPopup icon-content-white icon-content-white-ic_add_white_24dp'
        ).render()
    )
    web.template.body.append(web.popup.create('').render())
    return make_response(footer())

