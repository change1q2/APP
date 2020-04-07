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
import time

from appium.webdriver.common.touch_action import TouchAction

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
driver.implicitly_wait(10)

size = driver.get_window_size()
print(size)
width = size['width']
height = size['height']

class MobileKeys(object):
    ENTER = 66

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


    def jiugongge(self, elem, location):
        """九宫格绘制
        loction = [1,2,3,5,7]
        """
        if len(location) < 5:
            raise ValueError("location 需要至少5 个")

        size = elem.rect

        x = size['x']
        y = size['y']
        width = size['width']
        height = size['height']

        points = [
            {'x': x + width / 6 * 1, 'y': y + height / 6},
            {'x': x + width / 6 * 3, 'y': y + height / 6},
            {'x': x + width / 6 * 5, 'y': y + height / 6},
            {'x': x + width / 6 * 1, 'y': y + height / 6 * 3},
            {'x': x + width / 6 * 3, 'y': y + height / 6 * 3},
            {'x': x + width / 6 * 5, 'y': y + height / 6 * 3},
            {'x': x + width / 6 * 1, 'y': y + height / 6 * 5},
            {'x': x + width / 6 * 3, 'y': y + height / 6 * 5},
            {'x': x + width / 6 * 5, 'y': y + height / 6 * 5},
        ]

        # 绘制手势：TouchAction
        action = TouchAction(driver)
        # press(x=point1['x'], y= point1['y])
        # loction = [1, 2, 3, 5, 7]

        action.press(**points[location[0] - 1]).wait(200)
        for point in location[1:]:
            action.move_to(**points[point - 1]).wait(200)

        action.release().perform()

    def enter(self):
        """回车"""
        return self.driver.press_keycode(MobileKeys.ENTER)




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
    driver = Remote(desired_capabilities=caps, command_executor='http://127.0.0.1:4444/wd/hub')
    driver.implicitly_wait(10)

    # 快速切换页面
    driver.start_activity('com.xxzb.fenwoo', 'com.xxzb.fenwoo.activity.user.CreateGesturePwdActivity')

    driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()

    # 定位绘制手势的元素
    jiugongge_elem = driver.find_element_by_id('com.xxzb.fenwoo:id/gesturepwd_create_lockview')
    # 手势绘制,  1,2,3,5,7
    # 得到元素的起点坐标和高宽  {"x": 3, "y": 3, "width": 599, "height": 900}
    # e.rect
    # driver.get_window_size()
    # e.locatoin, 元素的坐标， e.size 获取宽度和高度
    BasePage(driver).jiugongge(jiugongge_elem, location=[1,2,3,5,8])