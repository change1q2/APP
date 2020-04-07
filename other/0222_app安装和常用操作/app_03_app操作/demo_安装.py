#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
"""
noReset:   reset: 重置应用，相当于首次打开app,  noreset: 不重置。




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
    "noReset": "false",
}

# 增量开发（编程）
driver = Remote(desired_capabilities=caps, command_executor='http://127.0.0.1:4444/wd/hub')
driver.implicitly_wait(10)
# 没有等待

# 包名
print(driver.current_package)

# 进入的activity
print(driver.current_activity)

# page_source
print(driver.page_source)

# 获取 app 屏幕大小
print(driver.get_window_size())

# 原生app没用，
# print(driver.current_window_handle)


time.sleep(5)

# 滑屏操作
for i in range(3):
    driver.swipe(600, 500, 10, 500)
    # app 测试当中和 web 自动化测试不同在于 app 容易崩。
    time.sleep(0.2)

# 点击立即进入
# driver.find_element_by_id('com.xxzb.fenwoo:id/btn_start')
# uiautomator
start_btn = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xxzb.fenwoo:id/btn_start")')
start_btn.click()

# 首页元素定位
my = driver.find_element_by_xpath('//android.widget.TextView[@text=\"我\"]')
my.click()

# 一定要手动关闭，不然会出现：1 ，设备找不到；2， viewer 不能截屏了。
driver.quit()



