import os

from scaffold.core.data.select import select_data
from scaffold.core.data.insert import insert_data
#~ from scaffold.core.data.update import update_data
#~ from scaffold.core.data.delete import delete_data
from scaffold.core.data.sql import query_builder

query_builder.query_path = os.path.abspath('./data/sql/')

class get_pledge(select_data):
    debug = True
    table = 'pledges'
    columns = {'id', 'name', 'total'}
    required = {'name'}

class get_pledges(select_data):
    debug = True
    #~ table = 'pledges'
    query_file = 'pledge_totals.sql'
    required = {'environment'}
    columns_where = {'expired', 'environment'}
    grouping = {'name'}

class add_pledge(insert_data):
    debug = True
    table = 'pledges'
    required = {'name'}
    columns = {'name'}

class add_payment(insert_data):
    debug = True
    table = 'pledge_amounts'
    required = {'pledge_id', 'reference', 'amount', 'environment'}
    columns = {'pledge_id', 'reference', 'amount', 'environment'}


