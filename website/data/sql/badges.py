import os
import time
from collections import defaultdict
from scaffold.core.data.select import select_data
from scaffold.core.data.insert import insert_data
from scaffold.core.data.update import update_data
from scaffold.core.data.delete import delete_data
from scaffold.core.data.sql import query_builder

query_builder.query_path = os.path.abspath('./data/sql/')


class create_badge(insert_data):
    table = 'badges'
    required = {'name'}
    columns = {'name'}

class assign_badge(insert_data):
    table = 'user_badges'
    required = {'user_id', 'badge_id'}
    columns = {'user_id', 'badge_id'}

class fetch_badges(select_data):
    #~ debug = True
    table = 'badges'
    columns = {'id', 'name'}

class fetch_badge(select_data):
    #~ debug = True
    table = 'user_badges'
    required = {'user_id'}
    columns = {'user_id', 'badge_id'}
    columns_where = {'user_id', 'badge_id'}
    columns_optional_where = {'user_id', 'badge_id'}
    columns_optional = {'user_id', 'badge_id'}

class fetch_user_badges(select_data):
    #~ debug = True
    table = 'user_badges'
    columns = {'user_id', 'badge_id'}
    #~ columns_where = {'user_id'}
    columns_optional_where = {'user_id', 'badge_id'}
    #~ columns_optional = {'user_id', 'badge_id'}

def fetch_user_badges_grouped():
    badge_lookup = defaultdict(list)
    for badge in fetch_user_badges():
        badge_lookup[badge.get('user_id')].append(badge.get('badge_id'))
    return badge_lookup

class remove_badge(delete_data):
    table = 'user_badges'
    required = {'id'}
    columns = {'id'}
