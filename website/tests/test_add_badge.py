#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import unittest
from collections import defaultdict

from config import settings

from data.badges import create_badge, assign_badge, remove_badge, fetch_badge, fetch_user_badges_grouped

from scaffold.core.data.database import db
from tests.base import TestBase

import unittest

class TestBadges(TestBase):

    def setUp(self):
        super(TestBadges, self).setUp()
        create_badge().execute({'name': 'member'})
        create_badge().execute({'name': 'backer'})
        create_badge().execute({'name': 'teacher'})
        create_badge().execute({'name': 'chairman'})
        create_badge().execute({'name': 'treasurer'})
        create_badge().execute({'name': 'secretary'})
        assign_badge().execute({'badge_id': '1', 'user_id': '1' })
        assign_badge().execute({'badge_id': '2', 'user_id': '1' })
        assign_badge().execute({'badge_id': '3', 'user_id': '1' })

    def testFetchUserBadges(self):
        self.assertTrue([a for a in fetch_badge({'badge_id': '1', 'user_id': '1' })])

    def test_badge_grouping(self):
        self.assertEquals(fetch_user_badges_grouped(),{1L: [1L, 2L, 3L]} )

    def testSelectingBadges(self):
        # this record should exist
        self.assertTrue([a for a in fetch_badge({'badge_id': '1', 'user_id': '1' })])
        
        # these don't exist
        self.assertFalse([a for a in fetch_badge({'badge_id': '10', 'user_id': '10' })])
        self.assertFalse([a for a in fetch_badge({'user_id': '10'})])

    def assignBadgeToUser(self):
        assign_badge().execute({'badge_id': '1', 'user_id': '1' })
        assign_badge().execute({'badge_id': '1', 'user_id': '1' })
        assign_badge().execute({'badge_id': '2', 'user_id': '1' })
        assign_badge().execute({'badge_id': '3', 'user_id': '1' })

    def testAddingBadges(self):
        create_badge().execute({'name': 'badget'})
        self.assertEquals(fetch_user_badges_grouped(),{1L: [1L, 2L, 3L]} )

    def testRemoveBadges(self):
        remove_badge().execute({'id': '1' })
        remove_badge().execute({'id': '2' })
        remove_badge().execute({'id': '3' })

if __name__ == '__main__':
    unittest.main(buffer=False)

