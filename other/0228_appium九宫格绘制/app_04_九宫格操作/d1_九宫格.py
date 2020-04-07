#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
滑屏：
1， 滑屏之前，进入app, 要等待。
2， 如果出现多次滑屏，每一次滑屏操作之间，要等待。
3， 滑屏需要提供至少 4 个参数，所以要进行封装，封装以后只需要传一个参数；甚至不需要传参数


九宫格：

acti
com.xxzb.fenwoo.activity.user.CreateGesturePwdActivity
"""

import time

from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction

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
driver = Remote(desired_capabilities=caps, command_executor='http://127.0.0.1:4723/wd/hub')
driver.implicitly_wait(10)

# 快速切换页面
driver.start_activity('com.xxzb.fenwoo', 'com.xxzb.fenwoo.activity.user.CreateGesturePwdActivity')

driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()


# 定位绘制手势的元素
jiugongge = driver.find_element_by_id('com.xxzb.fenwoo:id/gesturepwd_create_lockview')
# 手势绘制,  1,2,3,5,7
# 得到元素的起点坐标和高宽  {"x": 3, "y": 3, "width": 599, "height": 900}
# e.rect
# driver.get_window_size()
# e.locatoin, 元素的坐标， e.size 获取宽度和高度
size = jiugongge.rect
print(size)


x = size['x']
y = size['y']
width = size['width']
height = size['height']

point1 = {'x': x + width / 6 * 1, 'y': y + height / 6}
point2 = {'x': x + width / 6 * 3 , 'y': y + height / 6}
point3 = {'x': x + width / 6 * 5 , 'y': y + height / 6}
point5 = {'x': x + width / 6 * 3 , 'y': y + height / 6 * 3}
point7 = {'x': x + width / 6 * 1 , 'y': y + height / 6 * 5}

# 绘制手势：TouchAction
action = TouchAction(driver)
# press(x=point1['x'], y= point1['y])
action.press(**point1).wait(200).\
    move_to(**point2).wait(200).\
    move_to(**point3).wait(200).\
    move_to(**point5).wait(200).\
    move_to(**point7).wait(200).\
    release().perform()


time.sleep(2)
driver.quit()


