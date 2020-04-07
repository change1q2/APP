#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
"""
noReset:   reset: 重置应用，相当于首次打开app,  noreset: 不重置。

start_activity:
作用1: 快速进入某个页面
作用2： app 跳转



"""




# from selenium.webdriver import Chrome
import time

from appium.webdriver import Remote

from selenium.webdriver import Chrome

caps = {
    "platformName": "Android",
    # automationName: 平台原生测试框架
    # "automationName": "UiAutomator1",
    # "platformVersion": "5.1",
    # "app": r"‪D:\data\柠檬班环境\app测试环境\环境\应用apk包\Future-release-2018.apk",
    "deviceName": "Android Emulator",
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
    "appPackage": "com.xxzb.fenwoo",
    # "noReset": "false",
}

# 增量开发（编程）
driver = Remote(desired_capabilities=caps, command_executor='http://127.0.0.1:4444/wd/hub')
driver.implicitly_wait(10)


time.sleep(5)
# 快速进入登录页面
driver.start_activity('com.xxzb.fenwoo', 'com.xxzb.fenwoo.activity.addition.LoginActivity')


# 重置应用
# driver.reset()
# # 后台运行
# driver.background_app(5)
#
# # 判断app是否被安装
# if not driver.is_app_installed('com.lemon.lemonban'):
#     driver.install_app('.apk')
#
# driver.close_app()

driver.quit()


