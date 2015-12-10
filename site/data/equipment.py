import os
import time
import sys
sys.path.append(os.path.abspath('../../../../scaffold/'))
sys.path.insert(0,os.path.abspath('../../../../scaffold/'))
from scaffold.core.data.select import select_data
from scaffold.core.data.insert import insert_data
from scaffold.core.data.update import update_data
from scaffold.core.data.delete import delete_data
from scaffold.core.data.sql import query_builder

query_builder.query_path = os.path.abspath('./data/sql/')

class create(insert_data):
    table = 'requests'
    required = {'user_id', 'name'}
    columns = {'user_id', 'name'}
    columns_optional = {'price', 'description', 'url'}

class update(update_data):
    #~ debug = True
    table = 'requests'
    required = {'id', 'user_id'}
    columns = {'user_id', 'name'}
    columns_where = {'id'}
    columns_optional = {'price', 'description', 'url'}

class get_requests(select_data):
    debug = True
    #~ limit_rows = False
    pagination_rows = 100
    required = {}
    #~ query_str = 'select  id, user_id, name, description, url, price, count(user_id) as quantity from maidstone_hackspace.requests group by name'
    query_str = 'select  id, user_id, name, description, url, price as quantity from maidstone_hackspace.requests order by name'
    columns = {}
    

class get_request(select_data):
    table = 'requests'
    required = {'id'}
    columns = {'*'}
    #query_str = 'select  id, user_id, name, description, url, price, count(user_id) as quantity from maidstone_hackspace.requests group by name'
    columns_where = {'id'}
    #columns = {}
    
