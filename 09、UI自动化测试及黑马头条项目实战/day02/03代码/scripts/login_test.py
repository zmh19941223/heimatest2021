import time
import unittest


# 定义测试类
from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By
case_data = [("", "123456", "8888", "用户名不能为空"),
             ("13011113333", "", "8888", "密码不能为空"),
             ("13011113333", "123456", "", "验证码不能为空")]


class TestLogin(unittest.TestCase):
    # 类级别fixture初始化操作
    @classmethod  # 类级别的方法可以直接调用，不需要实例化对象(类)
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        webdriver.Firefox()
        cls.driver.maximize_window()

    # 方法级别的fixture
    def setUp(self):
        self.driver.get("http://tpshop-test.itheima.net/Home/Index/index.html")

    # 类级别fixture销毁操作
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 定义测试方法  登录操作  用户名为空
    @parameterized.expand(case_data)
    def test_login_01(self, mobile, password, code, expect):
        # 在首页中点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR, ".red").click()
        # 在登录页面中输入手机号码
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys(mobile)
        # 在登录页面中输入密码
        self.driver.find_element(By.ID, "password").send_keys(password)
        # 在登录页面中输入验证码
        self.driver.find_element(By.CSS_SELECTOR, ".check_cum>.text_cmu").send_keys(code)
        # 点击登录
        self.driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()
        time.sleep(1)
        # 获取错误提示信息
        msg = self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-content").text
        print("获取弹出框的信息:", msg)
        # 断言提示信息
        self.assertIn(expect, msg)
        time.sleep(1)
        # driver.quit()

        # 密码为空
    # def test_login_02(self):
    #     # driver = webdriver.Chrome()
    #     # driver.maximize_window()
    #     # driver.get("http://tpshop-test.itheima.net/Home/Index/index.html")
    #     # 在首页中点击登录按钮
    #     self.driver.find_element(By.CSS_SELECTOR, ".red").click()
    #     # 在登录页面中输入手机号码
    #     self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("13011113333")
    #     # 在登录页面中输入密码
    #     self.driver.find_element(By.ID, "password").send_keys("")
    #     # 在登录页面中输入验证码
    #     self.driver.find_element(By.CSS_SELECTOR, ".check_cum>.text_cmu").send_keys("8888")
    #     # 点击登录
    #     self.driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()
    #     time.sleep(1)
    #     # 获取错误提示信息
    #     msg = self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-content").text
    #     # 断言提示信息
    #     self.assertIn("密码不能为空", msg)
    #     time.sleep(2)
    #     # driver.quit()
