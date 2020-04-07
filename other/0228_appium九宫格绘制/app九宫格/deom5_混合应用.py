

from appium.webdriver import Remote



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

    driver = Remote(desired_capabilities=caps, command_executor='http://127.0.0.1:4444/wd/hub')
    driver.implicitly_wait(10)

    # iframe,web页面的切换
    # driver.switch_to.frame()

#手机的切换
    # 获取所有的上下文。（webview, native） 列表
    driver.contexts
    # webview_name, webview 的名字
    driver.switch_to.context('webview')
    # 进入到 网页。

