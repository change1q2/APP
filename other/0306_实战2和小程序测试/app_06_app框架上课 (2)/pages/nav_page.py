#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage


class NavPage(BasePage):
    """导航栏。
    属于多个页面。
    """
    # 元素定位器
    home_locator = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_home')
    tiku_locator = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_tiku')
    my_locator = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_my')

    # def get_element_nav(self):


    def click_nav(self, page_name):
        """进入对应页面.
        首页， 题库， 我的柠檬
        """
        if page_name == '首页':
            # 点击首页
            self.driver.find_element(*self.home_locator).click()
        elif page_name == '题库':
            self.driver.find_element(*self.tiku_locator).click()
        elif page_name == '我的柠檬':
            self.driver.find_element(*self.my_locator).click()
        else:
            raise ValueError("没有该导航")
