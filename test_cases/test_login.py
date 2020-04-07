#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import pytest

from data.login_data import login_empty
from pages.nav_page import NavPage
from pages.user_page import UserPage


class TestLogin:

    @pytest.mark.parametrize("test_info", login_empty)
    def test_login_empty(self, test_info, init_app):
        """"测试为空"""
        # 1， 点击我的柠檬
        # 2， 点击头像登录
        # 3， 登录页面输入用户名和密码
        # 4， 断言
        driver = init_app
        # 进入我的柠檬
        NavPage(driver).click_nav('我的柠檬')

        # 登录
        user_page = UserPage(driver)
        user_page.login(test_info['mobile'], test_info['pwd'])
        # 断言
        assert user_page.get_elem_toast(test_info['expected'])


    def test_login_empty(self, init_app):
        pass

