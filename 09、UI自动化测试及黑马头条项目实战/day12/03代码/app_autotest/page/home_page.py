# 首页面对象
# 定义对象库层
from selenium.webdriver.common.by import By

from app_autotest.base.base import BasePage, BaseHandle


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 我的  按钮
        self.me_btn = By.XPATH, "//*[@text='我的']"

    # 获取 我的 按钮元素
    def find_me_btn(self):
        return self.get_element(self.me_btn)


# 定义操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    # 对我的 按钮进行点击
    def click_me_btn(self):
        self.home_page.find_me_btn().click()


# 定义业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 点击我的按钮跳转到我的页面
    def go_me_page(self):
        self.home_handle.click_me_btn()
