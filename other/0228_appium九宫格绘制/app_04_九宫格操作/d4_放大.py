#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

multiaction = MultiAction(driver)

a1 = TouchAction(driver)
a1.move_to()


a2 = TouchAction(driver)
a2.move_to()

# 添加
multiaction.add(a1, a2)
multiaction.perform()
