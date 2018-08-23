# -*- coding:utf-8 -*-
#date:  2018/7/5


from lib.appController import Controller
from lib.log import logger
from caseTest.case_test import AppDemo
from conf.setting import *
import unittest
from lib.result import Result


class App(object):
    def __init__(self):
        self.controller = Controller()

    def case(self):
        #通过导入测试类来实现生成测试集
        suite = unittest.TestLoader().loadTestsFromTestCase(AppDemo)
        #实例化结果对象
        #生成一个空的结果集
        r = Result()

        #运行case，并更新结果集，记录正确的case 失败的case

        res = suite.run(r)

    def run(self):
        self.controller.server()
        driver = self.controller.driver()
        t = self.case()


if __name__ == '__main__':
    App().run()

