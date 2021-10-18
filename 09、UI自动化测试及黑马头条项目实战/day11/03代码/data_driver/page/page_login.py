# 表示的登录页面对象
from selenium.webdriver.common.by import By
from data_driver.base.base_page import BasePage, BaseHandle
from data_driver.utils import UtilsDriver


# 对象库层
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.username = By.ID, "username"  # 用户名输入框
        self.password = By.ID, "password"  # 密码输入框
        self.code = By.ID, "verify_code"   # 验证码输入框
        self.login_btn = By.CSS_SELECTOR, ".J-login-submit"  # 表示的是登录按钮

    # 用户名输入框
    def find_username(self):
        return self.get_element(self.username)
        # return self.driver.find_element(*self.username)

    # 密码输入框
    def find_password(self):
        return self.get_element(self.password)
        # return self.driver.find_element(*self.password)

    # 验证码输入框
    def find_code(self):
        return self.get_element(self.code)
        # return self.driver.find_element(*self.code)

    # 登陆按钮
    def find_login(self):
        return self.get_element(self.login_btn)
        # return self.driver.find_element(*self.login_btn)


# 操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)
        # self.login_page.find_username().clear()
        # self.login_page.find_username().send_keys(username)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)
        # self.login_page.find_password().clear()
        # self.login_page.find_password().send_keys(password)

    # 输入验证码
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)
        # self.login_page.find_code().clear()
        # self.login_page.find_code().send_keys(code)

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