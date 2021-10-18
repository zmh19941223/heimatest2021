import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.skip(reason="大于2.0的版本不需要再执行此用例")
class TestLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://tpshop-test.itheima.net/")
        self.driver.find_element(By.CSS_SELECTOR, ".red").click()

    def setup(self):
        self.driver.refresh()
        # self.driver.get("http://tpshop-test.itheima.net/Home/user/login.html")

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

    def test_login_01(self):  # 实现登录时用户名为空

        # 输入用户名 输入密码 输入验证码
        self.driver.find_element(By.ID, "username").send_keys(" ")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        # 点击登陆
        self.driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()

        msg = self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-content").text
        assert "用户名不能为空" in msg

    def test_login_02(self):  # 实现登录时密码为空

        # 输入用户名 输入密码 输入验证码
        self.driver.find_element(By.ID, "username").send_keys("13012345678")
        self.driver.find_element(By.ID, "password").send_keys(" ")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        # 点击登陆
        self.driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()

        msg = self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-content").text
        assert "密码不能为空" in msg

