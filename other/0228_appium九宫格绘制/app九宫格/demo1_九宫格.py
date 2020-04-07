'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
#com.xxxzb.fenwoo','com.xxzb.fenwoo.activity.addition.LoginActivity'

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

#快速切换页面
driver.start_activity('com.xxzb.fenwoo', 'com.xxzb.fenwoo.activity.user.CreateGesturePwdActivity')


driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()

# 定位绘制手势的元素
jiugongge = driver.find_element_by_id("com.xxzb.fenwoo:id/gesturepwd_create_lockview")
time.sleep(5)
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