# 表示的首页面对象


from selenium.webdriver.common.by import By

from V4.utils import UtilsDriver


# 对象库层  主要用来定位元素
class PageHome:
    def __init__(self):
        self.driver = UtilsDriver.get_driver()  # 浏览器驱动对象

    def find_login_btn(self):
        # 登录按钮
        return self.driver.find_element(By.CSS_SELECTOR, '.red')


# 操作层
class HandleHome:
    def __init__(self):
        # 实例化对象库层
        self.home_page = PageHome()

    # 点击登录按钮，跳转到登录页面
    def click_login_bin(self):
        self.home_page.find_login_btn().click()


# 业务层
class HomeProxy:
    def __init__(self):
        # 实例化操作层对象
        self.home_handle = HandleHome()

    # 点击登录按钮跳转到登录页面
    def go_login_page(self):
        self.home_handle.click_login_bin()
