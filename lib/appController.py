# -*- coding:utf-8 -*-
from conf.setting import Configure
from lib.log import logger
from appium import webdriver


class Controller(object):
    def __init__(self):
        self.yml = Configure().app_data
        self.devices = self.yml.get('devices')
        self.tester = self.yml.get('tester')
        self.device_type = self.yml.get('device_type')
        self.threads_server = []
        self.threads_driver = []
        self.ports = []

    #启动appium服备务
    def server(self):
        for device in self.devices.get(self.device_type):
            # 提取校验服务启动成功的端口
            self.ports.append(device.get('port'))

            logger.debug('配置参数：%s'%device)
            tt = self.server_commond(kwargs=device)

    def server_commond(self,**kwargs):
        commond = 'appium -a {ip} -p {port} -U {udid}'.format(ip=kwargs['kwargs'].get('ip'),
                                                                    port=kwargs['kwargs'].get('port'),
                                                                    udid=kwargs['kwargs'].get('udid')
                                                                    )
        logger.info('启动服务：{}'.format(commond))

    #启动手机设备
    def driver(self):
        #循环每一个手机配置
        for device in self.devices.get(self.device_type):


            device.update(self.tester)

            # logger.info("配置参数：%s"%device)

            dd = self.driver_comment(kwargs=device)

    def driver_comment(self,**kwargs):
        desired_caps = {'platformName': '', 'platformVersion': '', 'deviceName': '',
                                     "unicodeKeyboard": "True",
                                     "resetKeyboard": "True", 'udid': '', 'noReset': 'True'}
        #更新配置文件
        desired_caps.update(kwargs['kwargs'])
        logger.info('更新后的配置：%s'%desired_caps)

        url = 'http://{ip}:{port}/wd/hub'.format(port = desired_caps.get('port'),
                                                 ip=desired_caps.get('ip'))

        driver = webdriver.Remote(url,desired_caps)





if __name__ == '__main__':
    # Controller().server()
    Controller().driver()