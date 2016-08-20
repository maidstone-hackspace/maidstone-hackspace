#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import unittest

from werkzeug.security import generate_password_hash, check_password_hash

from config import settings
from data import site_user
from scaffold.core.data.database import db


class TestBasePage(unittest.TestCase):
#~ class TestBasePage(TestDataSetup):

    def testCreateBasicUser(self):
        """User has not signed up yet but has interacted with the site, donated perhaps ?"""
        site_user.create_basic_user().execute({
            'first_name': 'myfirstname',
            'last_name': 'mylastname'
        })

    def testCreateNormalUser(self):
        pw_hash = generate_password_hash('letmein')
        site_user.create().execute({
            'username': 'test@test.com',
            'first_name': 'myfirstname',
            'last_name': 'mylastname',
            'password': pw_hash
        })

    def testCreateDuplicateUsers(self):
        pw_hash = generate_password_hash('letmein')
        site_user.create().execute({
            'username': 'test@test.com',
            'first_name': 'myfirstname',
            'last_name': 'mylastname',
            'password': pw_hash
        })

        site_user.create().execute({
            'username': 'test@test.com',
            'first_name': 'myfirstname',
            'last_name': 'mylastname',
            'password': pw_hash
        })

    def testRegisterNewUser(self):
        pw_hash = generate_password_hash('letmein')
        site_user.create().execute({
            'username': 'new_user@test.com',
            'first_name': 'myfirstname',
            'last_name': 'mylastname',
            'password': pw_hash
        })

        user_details = site_user.get_by_username({
            'username': 'new_user@test.com'}).get()
        self.assertTrue(user_details)
        self.assertTrue(pw_hash == user_details.get('password'))
        self.assertTrue(user_details)
        

    def testRegisteringExistingUser(self):
        pw_hash = generate_password_hash('letmein')
        site_user.create().execute({
            'username': 'test@test.com',
            'first_name': 'myfirstname',
            'last_name': 'mylastname',
            'created': '',
            'password': pw_hash
        })

    def testChangeUserPassword(self):
        site_user.change_password().execute({
            'id': '1', 
            'password': 'password hash'
        })

    def testUpdateLastLogin(self):
        site_user.update_last_login().execute({
            'id': '1'
        })


if __name__ == '__main__':
    unittest.main(buffer=False)

