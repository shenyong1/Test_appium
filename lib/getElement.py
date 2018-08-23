# -*- coding:utf-8 -*-
#date:  2018/7/6

from conf.setting import Configure
from lib.log import logger

class GetElement(object):
    def __init__(self):
        self.yml = Configure().app_element_data

    def get_element_name(self,name):
        try:
            ele = self.yml.get(name)
            logger.info(ele)

            return ele
        except Exception as e:
            logger.error('获取配置文件：element_test.yml中属性失败！！！')


if __name__ == '__main__':
    GetElement().get_element_name('房态')