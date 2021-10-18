# 登录页面对象
# 定义对象库层
import time
from os import system

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from app_autotest.base.base import BasePage, BaseHandle
from app_autotest.utils import UtilsDriver


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 手机号输入框
        self.mobile = By.ID, "com.bjcsxq.chat.carfriend:id/login_phone_et"
        # 密码输入框
        self.password = By.ID, "com.bjcsxq.chat.carfriend:id/login_pwd_et"
        # 登录按钮
        self.login = By.ID, "com.bjcsxq.chat.carfriend:id/login_btn"
        # 提示信息
        self.msg = By.ID, "com.bjcsxq.chat.carfriend:id/txt_msg"
        # 确定按钮
        self.confirm = By.ID, "com.bjcsxq.chat.carfriend:id/btn_pos"

    # 查找手机号输入框
    def find_mobile(self):
        return self.get_element(self.mobile)

    # 查找密码输入框
    def find_password(self):
        return self.get_element(self.password)

    # 查找登录按钮
    def find_login(self):
        return self.get_element(self.login)

    # 查找提示信息框
    def find_msg(self):
        return self.get_element(self.msg)

    # 查找确定按钮
    def find_confirm(self):
        return self.get_element(self.confirm)


# 定义操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 输入手机号码
    def input_mobile(self, mobile):
        self.input_text(self.login_page.find_mobile(), mobile)

    # 输入密码
    def input_password(self, password):
        TouchAction(UtilsDriver.get_app_driver()).tap(x=200, y=750).perform()
        time.sleep(1)
        system("adb shell input text {}".format(password))
        # self.input_text(self.login_page.find_password(), password)

    # 点击登录按钮
    def click_login(self):
        self.login_page.find_login().click()

    # 获取提示信息
    def get_msg(self):
        return self.login_page.find_msg().text

    # 点击确定
    def click_confirm(self):
        self.login_page.find_confirm().click()


# 定义业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 实现登录功能
    def login(self, mobile, password):
        self.login_handle.input_mobile(mobile)  # 输入手机号
        self.login_handle.input_password(password)  # 输入密码
        self.login_handle.click_login()  # 点击登录

    # 定义一个获取弹出框消息的业务操作
    def get_tip_msg(self):
        msg = self.login_handle.get_msg()  # 获取弹出框信息
        # UtilsDriver.get_app_driver().refresh()
        self.login_handle.click_confirm()  # 点击确定按钮
        return msg

