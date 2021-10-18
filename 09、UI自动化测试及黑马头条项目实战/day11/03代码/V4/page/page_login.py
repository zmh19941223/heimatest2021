# 表示的登录页面对象

# 对象库层
from selenium.webdriver.common.by import By

from V4.utils import UtilsDriver


class LoginPage:
    def __init__(self):
        self.driver = UtilsDriver.get_driver()

    # 用户名输入框
    def find_username(self):
        return self.driver.find_element(By.ID, "username")

    # 密码输入框
    def find_password(self):
        return self.driver.find_element(By.ID, "password")

    # 验证码输入框
    def find_code(self):
        return self.driver.find_element(By.ID, "verify_code")

    # 登陆按钮
    def find_login(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".J-login-submit")


# 操作层
class LoginHandle:
    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    def input_username(self, username):
        self.login_page.find_username().send_keys(username)

    # 输入密码
    def input_password(self, password):
        self.login_page.find_password().send_keys(password)

    # 输入验证码
    def input_code(self, code):
        self.login_page.find_code().send_keys(code)

    # 点击登录按钮
    def click_login(self):
        self.login_page.find_login().click()


# 业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 实现登录功能
    def login(self, username, password, code):
        # 输入用户名
        self.login_handle.input_username(username)
        # 输入密码
        self.login_handle.input_password(password)
        # 输入验证码
        self.login_handle.input_code(code)
        # 点击登录按钮
        self.login_handle.click_login()