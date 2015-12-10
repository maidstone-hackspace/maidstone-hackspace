import os
import time
from scaffold.core.data.select import select_data
from scaffold.core.data.insert import insert_data
from scaffold.core.data.update import update_data
from scaffold.core.data.delete import delete_data
from scaffold.core.data.sql import query_builder

query_builder.query_path = os.path.abspath('./data/sql/')


class create(insert_data):
    table = 'users'
    required = {'email', 'password', 'username', 'first_name', 'last_name', 'created'}
    columns = {'email', 'password', 'username', 'first_name', 'last_name', 'created'}
    columns_optional = {'profile_image'}

    def calculated_data(self):
        return {'created': time.strftime('%Y-%m-%d %H:%M:%S')}

    def set(self, data):
        data['created'] = time.strftime('%Y-%m-%d %H:%M:%S')
        super(create, self).set(data)

class update_last_login(update_data):
    #~ table = 'users'
    debug = True
    query_str = "update `users` set `last_login`=now() where id=%(user_id)s"
    required = {'user_id'}
    #~ columns = {'id'}
    columns_where = {}

class delete_password_reset(delete_data):
    """clean up expired password resets"""
    table = 'user_password_reset'
    sql_where = 'where DATE_ADD(created, INTERVAL 1 HOUR) < now()'
    required = {}


class create_password_reset(insert_data):
    table = 'user_password_reset'
    required = {'user_id', 'reset_code'}

class get_user_by_reset_code(select_data):
    required = {'reset_code'}
    query_file = 'get_user_password_reset.sql'
    columns_where = ['reset_code']

class change_password(update_data):
    table = 'users'
    required = {'id', 'password'}
    columns_where = ['password']
    sql_where = 'id=%(id)s'


class get_users(select_data):
    required = {}
    query_file = 'get_users.sql'


class get_user_details(select_data):
    #~ debug = True
    required = {'id'}
    query_file = 'get_user_detail.sql'
    columns_where = {'users.id'}


class get_by_email(select_data):
    required = {'email'}
    query_file = 'get_users.sql'
    columns_where = {'email'}

class get_by_username(select_data):
    required = {'email'}
    query_file = 'get_user_credentials.sql'
    columns_where = {'email'}

class authorize(select_data):
    required = {'id'}
    query_file = 'get_user_credentials.sql'
    columns_where = {'id'}
