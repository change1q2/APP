#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
"""
app 的使用流程

安卓 sdk 环境：
1， adt-bundle, sdk_manager.exe, 更新非常不稳定
2， android studio,


如何顺利的讲 appium 启动起来：
1， appium, 雷电，（夜神）， pycharm
2,  cmd: adb devices, 确认设备是否在线
3,  appium 和 pycharm 当中端口号要对应。
4， 启动：uiautomator start error, stop uiautomator, UiAutomator2 或者直接去掉。
5， 获取包名和activity: aapt dump badging .apk


如何安装 app:
1, adb install ;
2, 手动拖到模拟器；


web 自动化测试代码原理：
Chrome(),  1, service.start();   2, remoteConnect, 初始化客户端。， 3， 类似requests发送接口请求。



appium 代码原理：


元素定位：
id,
name,
class_name
tag_name
link_text
partial_link_text
xpath
css_selector

html的构成：
- tagname
- 属性
- text
- 嵌套

app 是不是 html 写的呀？
在安卓当中，app 展示还是要使用标记性语言：xml

元素定位的辅助工具： web 自动化的 f12
- uiautomatorviewer, 包自带的元素定位辅助工具
- appium
- (weditor)

前提： adb devices, 有没有设备在线


元素定位辅助工具
- uiautomatorviewer
- appium
- weditor
appium-deskp


元素属性：
class_name,  组件类型，相当于 web 当中的 tagname
resource_id,  id


元素定位方式：
- id, app 当中的 id 不一定是唯一的。
- class_name
- xpath  (在 app 当中 text 是用 @text 表示， 不是 text() ,   )
- content-desc,   driver.find_element_by_accessibility_id()
- uiautomator,  find_element_by_android_uiautomator()
这个是安卓的原生定位方式，（快）



"""




# from selenium.webdriver import Chrome
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
    # "noReset": "false",
}

driver = Remote(desired_capabilities=caps, command_executor='http://127.0.0.1:4444/wd/hub')
# driver.find_element_by_accessibility_id()

# TODO: java 当中要用双引号表示字符串
# new UiSelector().className(\"android.widget.FrameLayout\").resourceId(\"com.lemon.lemonban:id/navigation_my\").clicable()
# driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.FrameLayout\").resourceId(\"com.lemon.lemonban:id/navigation_my\")')

driver.find_element