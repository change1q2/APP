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
#元素等待
driver.implicitly_wait(20)

#重置应用
driver.reset()
#后台运行
driver.background_app(5)

#判断APP是否存在
if not driver.is_app_installed('com.xxzb.fenwoo'):#包名
    driver.install_app('.apk')#APK路径

#关闭APP
driver.close_app()


driver.quit()