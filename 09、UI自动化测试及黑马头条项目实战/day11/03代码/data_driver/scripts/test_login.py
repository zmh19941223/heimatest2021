# 定义测试类
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from data_driver.utils import UtilsDriver, get_msg, get_case_data, case_data
from data_driver.page.page_home import HomeProxy
from data_driver.page.page_login import LoginProxy

login_case_data = case_data("./data_driver/case_data/login_case_data.json")


class TestLogin:
    def setup_class(self):
        # 实例化首页和登录的业务对象
        self.home_prxoy = HomeProxy()
        self.login_proxy = LoginProxy()
        # 通过首页页面的业务层操作实现登录的跳转
        self.home_prxoy.go_login_page()

    # 创建方法级别的fixture初始化的操作方法
    def setup(self):
        UtilsDriver.get_driver().refresh()

    # 创建类级别fixture销毁的操作方法
    def teardown_class(self):
        UtilsDriver.quit_driver()

    # 定义测试方法  账号不存在
    @pytest.mark.parametrize("username, password, code,expect", login_case_data)
    def test_login_01(self, username, password, code, expect):
        self.login_proxy.login(username,password,code)
        msg = get_msg()
        assert expect in msg
