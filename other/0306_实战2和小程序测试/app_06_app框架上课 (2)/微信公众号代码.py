from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy as MB

# 引入appium包
from appium import webdriver
import time


desired_caps = {}
# 支持X5内核应用自动化配置
desired_caps["recreateChromeDriverSessions"] = True
# android 4.4以下的版本通过Selendroid来切换到webview
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "8.1"
desired_caps["deviceName"] = "Android Emulator"
desired_caps["appPackage"] = "com.tencent.mm"
desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
desired_caps["chromedriverExecutableDir"] = 'C:\\wx_chromedriver'
desired_caps["noReset"] = True
desired_caps["unicodeKeyboard"] = True
# desired_caps["resetKeyboard"] = True

# ChromeOptions使用来定制启动选项，因为在appium中切换context识别webview的时候,
# 把com.tencent.mm:toolsmp的webview识别成com.tencent.mm的webview.
# 所以为了避免这个问题，加上androidProcess: com.tencent.mm:toolsm
desired_caps["chromeOptions"] = {"androidProcess": "com.tencent.mm:toolsmp"}
# desired_caps["browserName"] = ""

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver,30)

# 主页的元素
loc = (MB.ID,'com.tencent.mm:id/baj')
wait.until(EC.visibility_of_all_elements_located(loc))
time.sleep(3)

# 1、整个屏幕的大小 size
device_size = driver.get_window_size() # width  height
print(device_size)

# 找到订阅号信息  这个元素
old_page = None
new_page = driver.page_source
while old_page != new_page:
    # 等待并找元素
    loc = (MB.ANDROID_UIAUTOMATOR,'new UiSelector().text("订阅号消息").resourceId("com.tencent.mm:id/baj")')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
    except:
        # 如果不存在呢，滑动。页面的更新：更新前后页面的内容。
        driver.swipe(device_size["width"]*0.5,device_size["height"]*0.9,device_size["width"]*0.5,device_size["height"]*0.3,200)
        time.sleep(2)
        old_page = new_page
        new_page = driver.page_source
    else:
        driver.find_element(*loc).click()  # 点击订阅号进入
        break

# 点击柠檬班软件测试
loc = (MB.ANDROID_UIAUTOMATOR,'new UiSelector().text("柠檬班软件测试").resourceId("com.tencent.mm:id/a_0")')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 进入公众号页面 - 点一个链接进入
loc = (MB.ID,'com.tencent.mm:id/dd')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
eles = driver.find_elements(*loc)
eles[-1].click()

# web页面出现
time.sleep(3)
cons = driver.contexts
print("所有的上下文：",cons)

# 切换
driver.switch_to.context('WEBVIEW_com.tencent.mm:toolsmp')
time.sleep(3)
wins = driver.window_handles
print("所有的窗口",wins)
loc = (MB.XPATH,'//h2[@id="activity-name"]')  # 每篇文章的标题元素

# 循环查找所有的窗口
for win in wins:
    print(win)
    driver.switch_to.window(win)
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
    except:
        pass
    else:
        break

# 滑动html页面 --
time.sleep(2)
#driver.swipe(device_size["width"]*0.5,device_size["height"]*0.9,device_size["width"]*0.5,device_size["height"]*0.1,200)
loc = (MB.XPATH,'//p/img')
wait.until(EC.visibility_of_element_located(loc))
time.sleep(2)
# 获取当前页面的源码 - page_source
hs = driver.page_source
fs = open("html_source.html",mode="w",encoding='utf-8')
fs.write(hs)

element = driver.find_element(*loc)
driver.execute_script("arguments[0].scrollIntoView();",element)

