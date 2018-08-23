# -*- coding:utf-8 -*-
#date:  2018/7/6

import unittest
from lib.log import logger
from case.login import Case


class AppDemo(unittest.TestCase):
    def __repr__(self):
        return 'appdemo'

    @classmethod
    def setUpClass(cls):
        logger.info('setUpClass')
        cls.case = Case()

    def test_a(self):
        logger.info('test_a')
        self.case.fangtai()

    @classmethod
    def tearDownClass(cls):
        logger.info('tearDownClass')