#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import unittest
import random
from collections import defaultdict

sys.path.append(os.path.abspath('../'))

from config import settings
from scaffold.core.data.database import db
from data import site_user
from tests.test_data import clean, populate


class TestBase(unittest.TestCase):
    def setUp(self):
        clean()
        populate()
