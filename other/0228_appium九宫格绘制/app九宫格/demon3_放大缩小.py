'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

multiaction = MultiAction(driver)

a1 = TouchAction(driver)
a1.move_to()


a2 = TouchAction(driver)
a2.move_to()


#添加
multiaction.add(a1, a2)
multiaction.perform()