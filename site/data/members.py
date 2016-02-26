import os
from scaffold.core.data.select import select_data
#~ from scaffold.core.data.insert import insert_data
from scaffold.core.data.update import update_data
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

class fetch_member_badges(select_data):
    required = {'id'}
    query_file = 'fetch_user_badges.sql'
    columns_where = {'id'}

class update_membership_status(update_data):
    debug = True
    query_str = "update `users` set `status`=%(status)s where id=%(user_id)s"
    required = {'user_id', 'status'}
    columns_where = {}

class fetch_member_subscription(select_data):
    debug = True
    required = {'user_id'}
    query_str = 'select provider_id, subscription_reference from user_membership'
    columns_where = {'user_id'}
