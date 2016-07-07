#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import unittest
from collections import defaultdict

from config import settings
from scaffold.core.data.database import db
from data import site_user


class TestBasePage(unittest.TestCase):

    def test_fetch_non_existant_oauth_user(self):
        site_user.create_oauth_login().execute({
            'username': 'Non existant username',
            'provider': 1,
            'user_id': 1,
        })

    def test_fetch_existant_oauth_user(self):
        site_user.create_oauth_login().execute({
            'username': 'nick',
            'provider': 1,
            'user_id': 1,
        })

    def test_update_oauth_user(self):
        site_user.update_oauth_login().execute({
            'user_id': '2',
            'username': 'nick_modified',
            'provider': 3,
        })


if __name__ == '__main__':
    unittest.main(buffer=False)

