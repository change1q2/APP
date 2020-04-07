#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import pytest
import os

import yaml
from appium.webdriver import Remote

from config.constant import p_path
from config.security_config import corrent_username, corrent_pwd
from pages.nav_page import NavPage
from pages.user_page import UserPage

yaml_file = os.path.join(p_path.CONFIG_PATH, 'caps.yaml')
f = open(yaml_file)

caps = yaml.load(f, Loader=yaml.FullLoader)
f.close()
print(caps)


@pytest.fixture()
def init_app():
    """启动app fixture"""
    # caps = {
    #     "platformName": "Android",
    #     "deviceName": "Android Emulator",
    #     "automationName": "UiAutomator2",
    #     "appActivity": ".activity.MainActivity",
    #     "appPackage": "com.lemon.lemonban",
    #     "chromedriverExecutableDir" : r"C:\chrome_driver",
    #     "noReset": False,
    # }
    driver = Remote(desired_capabilities=caps, command_executor='http://127.0.0.1:4723/wd/hub')
    driver.implicitly_wait(20)
    yield driver

    print("退出浏览器")
    driver.quit()


@pytest.fixture()
def login(init_app):
    """登录的前置条件"""
    driver = init_app
    NavPage(driver).click_nav('我的柠檬')

    # 登录
    user_page = UserPage(driver)
    user_page.login(corrent_username, corrent_pwd)

    yield driver

    print("退出 login")






