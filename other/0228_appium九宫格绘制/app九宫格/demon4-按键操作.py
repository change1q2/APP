'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
import time

from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver import Chrome


class MobileKeys:
    ENTER = 66
    VOLUME_UP = 24
    VOLUME_DOWN = 25


if __name__ == '__main__':

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

    # 调用按键
    driver.press_keycode(MobileKeys.VOLUME_UP)
    driver.press_keycode(MobileKeys.VOLUME_UP)
    driver.press_keycode(MobileKeys.VOLUME_UP)
    driver.press_keycode(MobileKeys.VOLUME_UP)
    driver.press_keycode(MobileKeys.VOLUME_UP)

    driver.quit()

    driver.save_screenshot()
    # driver.send_keys()