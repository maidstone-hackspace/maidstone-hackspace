#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import unittest
import random
from collections import defaultdict
from werkzeug.security import generate_password_hash, check_password_hash


from config import settings
from scaffold.core.data.sql import query
from scaffold.core.data.database import db
from data import site_user

data_first_names = ['ralf', 'teddy', 'sprite']
data_last_names = ['fuzzie']



def clean():
    clean_file = os.path.abspath('./data/migrate/clean.sql')
    with open(clean_file, 'r') as clean_fp:
        sql = clean_fp.read()
        query().execute({}, sql)
    
def populate():
    site_user.create_basic_user().execute(data={
        'first_name': random.choice(data_first_names), 
        'last_name': random.choice(data_last_names),
        'password': generate_password_hash('test')
    })
