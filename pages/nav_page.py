'''
作者：seak
时间：
项目：
题目：
作用：
备注：
下方导航处于3个界面所以可以单独创建
'''
from appium.webdriver.common.mobileby import MobileBy
class NavPage:
    """
    导航栏
    属于多个界面

    """
    # 元素定位器
    home_locator = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_home')
    tiku_locator = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_tiku')
    my_locator = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_my')


    #方法