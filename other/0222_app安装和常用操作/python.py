'''
作者：seak
时间：
项目：
题目：
作用：
备注：
driver swipe滑屏
'''

from appium.webdriver import Remote
import time

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

# TODO: java 当中要用双引号表示字符串
# new UiSelector().className(\"android.widget.FrameLayout\").resourceId(\"com.lemon.lemonban:id/navigation_my\").clicable()
# driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.FrameLayout\").resourceId(\"com.lemon.lemonban:id/navigation_my\")')

#查找元素方式
#driver.find_element

#元素等待
driver.implicitly_wait(20)
windown_size = driver.get_window_size()
print(windown_size)
time.sleep(5)
#滑动,需要滑动3次
for i in range(3):
    driver.swipe(800,500,10,500)
    time.sleep(0.2)

#点击立即进入
#driver.find_element_by_id('com.xxzb.fenwoo:id/btn_start')
#java的写法uiautomator
start_btn = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xxzb.fenwoo:id/btn_start")')
start_btn.click()

#首页元素定位
my = driver.find_element_by_xpath('//android.widget.TextView[@text=\"我\"]')

#手动关闭
#driver.quit()