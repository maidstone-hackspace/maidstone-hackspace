import os
from scaffold.core.data.select import select_data
#~ from scaffold.core.data.insert import insert_data
#~ from scaffold.core.data.update import update_data
#~ from scaffold.core.data.delete import delete_data
from scaffold.core.data.sql import query_builder

query_builder.query_path = os.path.abspath('./data/sql/')


class get_members(select_data):
    required = {}
    query_file = 'member_list.sql'
    columns = {}


class get_member_profile(select_data):
    required = {'id'}
    query_file = 'get_users.sql'
    columns_where = {'id'}
