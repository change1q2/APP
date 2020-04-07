#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage


class UserPage(BasePage):
    """用户页面"""
    # 头像元素
    avatar_locator = (MobileBy.ID, 'com.lemon.lemonban:id/fragment_my_lemon_avatar_layout')
    login_btn_locator = (MobileBy.ID, 'com.lemon.lemonban:id/btn_login')
    mobile_locator = (MobileBy.ID, 'com.lemon.lemonban:id/et_mobile')
    pwd_locator = (MobileBy.ID, 'com.lemon.lemonban:id/et_password')

    def login(self, mobile, pwd):
        """登录"""
        # 点击头像
        self.get_element_avatar().click()
        # 输入手机号码
        self.get_element_mobile().send_keys(mobile)
        # 输入密码
        self.get_element_pwd().send_keys(pwd)
        # 点击登录
        self.get_elem_login_btn().click()

    def get_element_mobile(self):
        """获取手机号码元素"""
        return self.wait_element(self.mobile_locator)

    def get_element_pwd(self):
        """获取手机号码元素"""
        return self.wait_element(self.pwd_locator)

    def get_element_avatar(self):
        """头像"""
        return self.wait_element(self.avatar_locator)

    def get_elem_login_btn(self):
        return self.wait_element(self.login_btn_locator)
