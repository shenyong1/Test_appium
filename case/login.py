# -*- coding:utf-8 -*-
#date:  2018/7/5
from lib.commonTools import ComTools
import time

class Case():
    def __init__(self):
        self.baseePage = ComTools()

    def fangtai(self):
        self.baseePage.click('房态')
        time.sleep(5)
        self.baseePage.click('订单')