import os
import time

from scaffold.core.data.select import select_data
from scaffold.core.data.insert import insert_data
from scaffold.core.data.update import update_data
from scaffold.core.data.delete import delete_data
from scaffold.core.data.sql import query_builder

query_builder.query_path = os.path.abspath('./data/sql/')



class update_description(update_data):
    #~ debug = True
    table = 'user_detail'
    required = {'user_id', 'description', 'skills'}
    columns = {'user_id', 'description', 'skills'}

