from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage


class TikuPage(BasePage):
    """题库页面操作"""

    # 标题定位
    tiku_detail_title_locator = (MobileBy.ID, 'com.lemon.lemonban:id/category_title')
    # 题库定位
    tiku_locator = (MobileBy.ID, 'com.lemon.lemonban:id/fragment_category_type')

    def get_tiku(self, name):
        """根据名字获取题库元素. 养乐多"""
        # 如果滑动之前的源码和滑动之后的源码相等，滑动到底部。

        old_page = ''
        new_page = self.driver.page_source

        while old_page != new_page:
            try:
                e = self.driver.find_element_by_xpath("//*[contains(@text, '{}')]".format(name))
                return e
            except:
                self.swipe_up()
                old_page = new_page
                new_page = self.driver.page_source

        raise ValueError("没有这个题库")


    # def get_tiku_fast(self, name):
    #     """根据名字获取题库元素2"""
    #     old_page = ''
    #     new_page = self.driver.page_source
    #
    #     tiku = []
    #
    #     while old_page != new_page:
    #         # 查找第一页所有的题库
    #         elements = self.driver.find_elements(*self.tiku_locator)
    #         for e in elements:
    #             tiku.append(e.text)
    #             if name == e.text:
    #                 return e
    #         self.swipe_up()
    #         old_page = new_page
    #         new_page = self.driver.page_source
    #
    #     raise ValueError("没有这个题库")


    def get_element_tiku_title(self):
        """定位题库的标题"""
        return self.wait_element(self.tiku_detail_title_locator)