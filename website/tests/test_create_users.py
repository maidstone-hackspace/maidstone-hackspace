#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import unittest

from config import settings

from data import site_user
from scaffold.core.data.database import db
import unittest


class TestBasePage(unittest.TestCase):
#~ class TestBasePage(TestDataSetup):

    def testCreateBasicUser(self):
        """User has not signed up yet but has interacted with the site, donated perhaps ?"""
        site_user.create_basic_user().execute({
            'email': 'test@test.com',
            'first_name': 'myfirstname',
            'last_name': 'mylastname'
        })

    #~ def testCreateNormalUser(self):
        #~ site_user.create().execute({
            #~ 'email': 'test@test.com',
            #~ 'first_name': 'myfirstname',
            #~ 'last_name': 'mylastname'
        #~ })


if __name__ == '__main__':
    unittest.main(buffer=False)

