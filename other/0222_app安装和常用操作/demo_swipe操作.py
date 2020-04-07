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

from appium.webdriver import Remote

from selenium.webdriver import Chrome

caps = {
    "platformName": "Android",
    "automationName": "UiAutomator1",#平台原生测试框架
    #"platformVersion": "5.1", #只有一个手机时可以不用设置
    "deviceName": "emulator-5554",#手机名称，adb devices
    "app": r"E:\APP\环境\应用apk包\Future-release-2018.apk",  #自动安装apk
    "appActjvity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",#aapt dump badging     launchable-activity
    "appPackage": "com.xxzb.fenwoo", #包名#aapt dump badging
    "noReset": "false",

}

driver = Remote(desired_capabilities=caps, command_executor="http://127.0.0.1:4723/wd/hub")
# driver.find_element_by_accessibility_id()
#元素等待
driver.implicitly_wait(20)

size = driver.get_window_size()
print(size)
width = size['width']
height = size['height']

class BasePage:
    def __init__(self,driver):
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

    def swipe(self,direction):
        '''滑动
        swipe('left')'''

        swipe_action = {
            'left': self.swipe_left,
            'right': self.swipe_right,
            'up': self.swipe_up,
            'down': self.swipe_down
        }
        #swipe_cation['left'] = self.swipe_left
        if direction not in swipe_action:
            raise ValueError("参数不正确")
        return swipe_action[direction]()

    # def swipe_left_ext(self, scale=0.9):
    #     """向左滑动
    #     600 ==>  540   570, 30,
    #     600 ==>   540, 60
    #     share = 600 * (1 - 0.9) / 2   # 每 0.1 左边和右边要滑动的像素点
    #     right = 600 - share
    #     left = share
    #     """
    #     share = self.width() * (1 - scale) / 2
    #     return driver.swipe(self.width() - share , self.height() * 0.5, share, self.height() * 0.5)



# 原生app没用，
# print(driver.current_window_handle)


time.sleep(5)
#滑动,需要滑动3次
for i in range(3):
    #driver.swipe(windown_width*0.8,windown_height*0.5,windown_size*0.1,windown_height*0.5)
    page =BasePage(driver)
    page.swipe('left')
    time.sleep(0.2)


driver.quit()

