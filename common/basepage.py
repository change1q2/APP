#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/10/24 21:39
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
import logging
import os
import time

from datetime import datetime

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome

from config.constant import p_path


class BasePage():

    def __init__(self, driver: Chrome):
        self.driver = driver

    def wait_element(self, locator, timeout=30, frequcy=0.5):
        """等待元素出现。强制等待。 locator:(By.Xpath, '')"""
        used_time = 0
        while used_time < timeout:
            try:
                e = self.driver.find_element(*locator)
                time.sleep(frequcy)
                return e
            except NoSuchElementException:
                time.sleep(frequcy)
                used_time += frequcy
        logging.error("等待元素超时")
        # 截图保存, 使用单独的文件夹存储截图，截图名字加上时间戳
        self.driver.screen_shot()
        raise NoSuchElementException

    def wait_precence_elem(self, locator, timeout=30, frequcy=0.5):
        """等待元素出现，显示等待"""
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=frequcy)
            e = wait.until(EC.presence_of_element_located(locator))
            return e
        except TimeoutException:
            # 记录 logger = LoggerHandler()
            logging.error("等待元素超时")
            # 截图保存, 使用单独的文件夹存储截图，截图名字加上时间戳
            self.screen_shot()

    def screen_shot(self):
        """截图"""
        shot_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        shot_name = os.path.join(p_path.SCREEN_SHOT_PATH, shot_name+'.png')
        self.driver.save_screenshot(shot_name)

    def wait_click_elem(self, locator, timeout=30, frequcy=0.5):
        """等待元素出现，显示等待"""
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=frequcy)
            e = wait.until(EC.element_to_be_clickable(locator))
            return e
        except TimeoutException:
            # 记录 logger = LoggerHandler()
            logging.error("等待元素超时")
            # 截图保存, 使用单独的文件夹存储截图，截图名字加上时间戳
            self.screen_shot()

    def wait_visible_elem(self, locator, timeout=30, frequcy=0.5):
        """等待元素出现，显示等待"""
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=frequcy)
            e = wait.until(EC.visibility_of_element_located(locator))
            return e
        except TimeoutException:
            # 记录 logger = LoggerHandler()
            logging.error("等待元素超时")
            # 截图保存, 使用单独的文件夹存储截图，截图名字加上时间戳
            self.screen_shot()

    def right_click(self, on_element=None):
        """鼠标右击"""
        action = ActionChains(self.driver)
        return action.context_click(on_element).perform()

    def move_to(self, on_element=None):
        action = ActionChains(self.driver)
        return action.move_to_element(on_element).perform()

    def enter(self, elem):
        """回车"""
        return elem.send_keys(Keys.ENTER)

    def switch_window(self, window):
        """窗口切换"""
        pass

    def get_elem_toast(self, msg):
        """获取 toast 元素"""
        try:
            return self.driver.find_element(*(MobileBy.XPATH, '//*[contains(@text, {})]'.format(msg)))
        except:
            return False

    @property
    def width(self):
        """获取app的宽度"""
        return self.driver.get_window_size()['width']

    @property
    def height(self):
        """获取app的高度"""
        return self.driver.get_window_size()['height']

    def swipe_left(self, duration=200, swipes=1):
        for s in range(swipes):
            self.driver.swipe(self.width * 0.9, self.height * 0.5,
                              self.width * 0.1, self.height * 0.5, duration)

    def swipe_right(self, duration=200, swipes=1):
        for s in range(swipes):
            width = self.driver.get_window_size()['width']
            height = self.driver.get_window_size()['height']
            self.driver.swipe(width * 0.1, height * 0.5, width * 0.9, height * 0.5, duration)

    def swipe_up(self, duration=200, swipes=1):
        for s in range(swipes):
            width = self.driver.get_window_size()['width']
            height = self.driver.get_window_size()['height']
            self.driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1, duration)

    def swipe_down(self, duration=200, swipes=1):
        for s in range(swipes):
            width = self.driver.get_window_size()['width']
            height = self.driver.get_window_size()['height']
            self.driver.swipe(width * 0.5, height * 0.1, width * 0.5, height * 0.9, duration)


    def jiugongge(self, elem, location):
        """九宫格绘制
        loction = [1,2,3,5,7]
        """
        if len(location) < 5:
            raise ValueError("location 需要至少5 个")

        size = elem.rect

        x = size['x']
        y = size['y']
        width = size['width']
        height = size['height']

        points = [
            {'x': x + width / 6 * 1, 'y': y + height / 6},
             {'x': x + width / 6 * 3, 'y': y + height / 6},
            {'x': x + width / 6 * 5, 'y': y + height / 6},
             {'x': x + width / 6 * 1, 'y': y + height / 6 * 3},
             {'x': x + width / 6 * 3, 'y': y + height / 6 * 3},
             {'x': x + width / 6 * 5, 'y': y + height / 6 * 3},
            {'x': x + width / 6 * 1, 'y': y + height / 6 * 5},
            {'x': x + width / 6 * 3, 'y': y + height / 6 * 5},
            {'x': x + width / 6 * 5, 'y': y + height / 6 * 5},
        ]

        # 绘制手势：TouchAction
        action = TouchAction(self.driver)
        # press(x=point1['x'], y= point1['y])
        # loction = [1, 2, 3, 5, 7]

        action.press( **points[location[0] - 1]).wait(200)
        for point in location[1:]:
            action.move_to( **points[point - 1] ).wait(200)

        action.release().perform()


    def zoom(self, scale):
        """放大.   0.1,  高德地图，百度地图"""
        multiaction = MultiAction(self.driver)

        # 手指1
        finger_1 = TouchAction(self.driver)
        finger_1.press(self.width / 2, self.height / 2).\
            move_to( self.width / 2 - self.width * scale / 2 ,  self.height / 2)\
            .release()

        # 手指2
        finger_2 = TouchAction(self.driver)
        finger_2.press(self.width / 2, self.height / 2).wait(100). \
            move_to(self.width / 2 + self.width * scale / 2, self.height / 2) \
            .release()

        multiaction.add(finger_1, finger_2)
        multiaction.perform()


    def pinch(self, scale):
        "缩小"
        multiaction = MultiAction(self.driver)

        # 手指1
        finger_1 = TouchAction(self.driver)
        finger_1.press(self.width / 2 - self.width * scale / 2, self.height / 2). \
            move_to(self.width / 2, self.height / 2) \
            .release()

        # 手指2
        finger_2 = TouchAction(self.driver)
        finger_2.press(self.width / 2 + self.width * scale / 2, self.height / 2).wait(100). \
            move_to(self.width / 2 , self.height / 2) \
            .release()

        multiaction.add(finger_1, finger_2)
        multiaction.perform()


    def double_press(self,  el=None, x=None, y=None):
        """双击"""
        ac = TouchAction(self.driver)
        ac.press( el=None, x=None, y=None).wait(100).release().\
            wait(500).press(el=None, x=None, y=None).wait(100).release().\
            perform()

    # 鼠标操作
    # 键盘操作
    # 上传文件
    # 标签页管理
    # 窗口切换
    # iframe 切换
    #