#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/10/9 21:20
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
import os


class BasePath:
    pass


class Config(BasePath):
    # 项目路径
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 测试用例数据的路径
    DATA_PATH = os.path.join(ROOT_PATH, 'data')
    # 配置文件路径
    CONFIG_PATH = os.path.join(ROOT_PATH, 'config')
    # 测试用例方法路径
    CASE_PATH = os.path.join(ROOT_PATH, 'cases')
    # 测试报告路径
    REPORT_PATH = os.path.join(ROOT_PATH, 'reports')
    # 如果没有改文件夹，自动创建
    if not os.path.exists(REPORT_PATH):
        os.mkdir(REPORT_PATH)

    SCREEN_SHOT_PATH = os.path.join(ROOT_PATH, 'img')
    if not os.path.exists(SCREEN_SHOT_PATH):
        os.mkdir(SCREEN_SHOT_PATH)

    # 隐式等待超时时间
    IMPLICIT_WAIT_TIMEOUT = 30
    # chromedriver 路径
    DRIVER_PATH = r"C:\chrome_driver\chromedriver_77.exe"
    # HOST_URL
    HOST = "http://120.78.128.25:8765"
    # 正确的手机号 和 密码
    CORRECT_USER = {"mobile": "18173179913",  "pwd": "179913"}


p_path = Config()

