# 我的页面对象
from selenium.webdriver.common.by import By

from app_autotest.base.base import BasePage, BaseHandle


# 定义对象库层
class MinePage(BasePage):
    def __init__(self):
        super().__init__()
        # 登录/注册 按钮
        self.login_btn = By.ID, "com.bjcsxq.chat.carfriend:id/mine_username_tv"

    # 查找登录注册按钮的元素
    def find_login_btn(self):
        return self.get_element(self.login_btn)


# 定义操作层
class MineHandle(BaseHandle):
    def __init__(self):
        self.mine_page = MinePage()

    # 点击登录注册按钮
    def click_login_btn(self):
        self.mine_page.find_login_btn().click()


# 定义业务层
class MineProxy:
    def __init__(self):
        self.mine_handle = MineHandle()

    # 点击登录按钮跳转到登录页面
    def go_login_page(self):
        self.mine_handle.click_login_btn()