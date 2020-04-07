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
driver = Remote(desired_capabilities=caps, command_executor='http://127.0.0.1:4723/wd/hub')
driver.implicitly_wait(10)


size = driver.get_window_size()
print(size)
width = size['width']
height = size['height']


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def width(self):
        """获取屏幕宽度"""
        return self.driver.get_window_size()['width']

    def height(self):
        """获取屏幕高度"""
        return self.driver.get_window_size()['height']

    def swipe_left(self):
        """向左滑动
        """
        return driver.swipe(self.width() * 0.9 , self.height() * 0.5, self.width() * 0.1 , self.height() * 0.5)

    def swipe_right(self):
        """向右滑动"""
        return driver.swipe(self.width() * 0.1, self.height() * 0.5, self.width() * 0.9, self.height() * 0.5)

    def swipe_up(self):
        """想上"""
        return driver.swipe(self.width() * 0.5, self.height() * 0.9, self.width() * 0.5, self.height() * 0.1)

    def swipe_down(self):
        """想上"""
        return driver.swipe(self.width() * 0.5, self.height() * 0.1, self.width() * 0.5, self.height() * 0.9)

    def swipe(self, direction):
        """滑动。
        swipe('left')
        """
        # if direction == 'left':
        #     return self.swipe_left()

        swipe_action = {
            'left': self.swipe_left,
            'right': self.swipe_right,
            'up': self.swipe_up,
            'down': self.swipe_down
        }
        # swipe_action['left'] = self.swipe_left
        if direction not in swipe_action:
            raise ValueError("参数不正确")
        return swipe_action[direction]()

    def swipe_left_ext(self, scale=0.9):
        """向左滑动
        600 ==>  540   570, 30,
        600 ==>   540, 60
        share = 600 * (1 - 0.9) / 2   # 每 0.1 左边和右边要滑动的像素点
        right = 600 - share
        left = share
        """
        share = self.width() * (1 - scale) / 2
        return driver.swipe(self.width() - share , self.height() * 0.5, share, self.height() * 0.5)



# 原生app没用，
# print(driver.current_window_handle)


time.sleep(5)

# 滑屏操作
for i in range(3):
    page = BasePage(driver)
    page.swipe('left')
    # driver.swipe(width * 0.9 , height * 0.5 , width * 0.1, height * 0.5)
    # app 测试当中和 web 自动化测试不同在于 app 容易崩。
    time.sleep(0.2)


driver.quit()


