import pytest
from appium.webdriver.common.mobileby import MobileBy

from data.tiku_data import tiku_data
from pages.nav_page import NavPage
from pages.tiku_page import TikuPage


class TestTiku:



    @pytest.mark.parametrize("test_info", tiku_data)
    def test_tiku_name(self, test_info, login):
        """测试题库名称是否显示正确"""
        driver = login
        # 点击题库
        NavPage(driver).click_nav('题库')
        # 点击Linux题库
        tiku_page = TikuPage(driver)
        tiku_page.get_tiku(test_info['data']).click()

        assert test_info['expected'] == tiku_page.get_element_tiku_title().text



