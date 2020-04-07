'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''

from appium.webdriver import Remote
import time

# caps = {
#     "platformName": "Android",
#     "deviceName": "Android Emulator",
#     "automationName": "UiAutomator2",
#     "appActivity": ".activity.MainActivity",
#     "appPackage": "com.lemon.lemonban",
#     "chromedriverExecutableDir" : r"C:\chromdriver",
#     "noReset": False,
# }
#
# driver = Remote(desired_capabilities=caps, command_executor="http://127.0.0.1:4723/wd/hub")
# #元素等待
# driver.implicitly_wait(20)

def init_app():
    caps = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "appActivity": ".activity.MainActivity",
        "appPackage": "com.lemon.lemonban",
        "chromedriverExecutableDir": r"C:\chromdriver",
        "noReset": False,
    }

    driver = Remote(desired_capabilities=caps, command_executor="http://127.0.0.1:4723/wd/hub")
    # 元素等待
    driver.implicitly_wait(20)
init_app()