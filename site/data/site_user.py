import os
import time
from scaffold.core.data.select import select_data
from scaffold.core.data.insert import insert_data
from scaffold.core.data.update import update_data
from scaffold.core.data.delete import delete_data
from scaffold.core.data.sql import query_builder

query_builder.query_path = os.path.abspath('./data/sql/')


class create_basic_user(insert_data):
    """not able to actually log in but registered on the system"""
    table = 'users'
    required = {'email', 'first_name', 'last_name'}
    columns = {'email','first_name', 'last_name'}

    def calculated_data(self):
        return {'created': time.strftime('%Y-%m-%d %H:%M:%S')}

    def set(self, data):
        data['created'] = time.strftime('%Y-%m-%d %H:%M:%S')
        super(create_basic_user, self).set(data)

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

class update_membership_status(update_data):
    debug = True
    query_str = "update `users` set `status`=%(status)s where id=%(user_id)s"
    required = {'user_id', 'status'}
    columns_where = {}

class create_membership(insert_data):
    debug = True
    table = 'user_membership'
    required = {'user_id', 'subscription_reference', 'status', 'amount', 'join_date'}
    columns = {'user_id', 'subscription_reference', 'status', 'amount', 'join_date'}
    columns_where = {}

class update_membership(update_data):
    debug = True
    query_str = u"""
        update user_membership set 
            status=%(status)s, 
            subscription_reference=%(subscription_reference)s, 
            amount=%(amount)s, 
            join_date=%(join_date)s 
        where id=%(user_id)s"""
    required = {'subscription_reference', 'status', 'amount', 'join_date'}
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


class get_user_bio(select_data):
    #~ debug = True
    required = {'id'}
    query_file = 'get_user_bio.sql'
    columns_where = {'user_id'}

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


class create_oauth_login(insert_data):
    required = {'username', 'provider'}
    query_file = 'get_user_by_oauth_username.sql'
    columns_where = {'username', 'provider'}

    def calculated_data(self):
        return {'registered': time.strftime('%Y-%m-%d %H:%M:%S')}

    def set(self, data):
        data['registered'] = time.strftime('%Y-%m-%d %H:%M:%S')
        super(create, self).set(data)

class update_oauth_login(update_data):
    required = {'username', 'provider'}
    query_file = 'get_user_by_oauth_username.sql'
    columns_where = {'username', 'provider'}

    def calculated_data(self):
        return {'registered': time.strftime('%Y-%m-%d %H:%M:%S')}

    def set(self, data):
        data['registered'] = time.strftime('%Y-%m-%d %H:%M:%S')
        super(create, self).set(data)

class fetch_oauth_login(select_data):
    required = {'username', 'provider'}
    query_file = 'get_user_by_oauth_username.sql'
    columns_where = {'username', 'provider'}
