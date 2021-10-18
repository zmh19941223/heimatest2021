"""
定义接口测试用例
使用unittest
1.导包
2.创建测试类
    2.1 前置处理
    2.2 后置处理
    2.3.创建测试方法
"""

# 1.导包
import requests
import unittest
from api.login import LoginAPI


# 2.创建测试类
class TestLogin(unittest.TestCase):
    # 2.1 前置处理
    def setUp(self):
        self.login_api = LoginAPI()  # 实例化接口类
        self.session = requests.Session()  # 创建session对象

    # 2.2 后置处理
    def tearDown(self):
        if self.session:
            self.session.close()

    # 2.3.创建测试用例
    # 登录成功
    def test01_login_success(self):
        # 调用验证码接口获取验证，并进行断言
        response = self.login_api.get_verify_code(self.session)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))

        # 调用登录接口获取登录信息，并进行断言
        response = self.login_api.login(self.session, "13488888888", "123456", "8888")
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get("status"))
        self.assertIn("登陆成功", response.json().get("msg"))

    # 账号不存在
    def test02_user_is_not_exist(self):
        # 调用验证码接口获取验证，并进行断言
        response = self.login_api.get_verify_code(self.session)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))

        # 调用登录接口获取登录信息，并进行断言
        response = self.login_api.login(self.session, "13488888899", "123456", "8888")
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, response.json().get("status"))
        self.assertIn("账号不存在", response.json().get("msg"))

    # 密码错误
    def test03_password_error(self):
        # 调用验证码接口获取验证，并进行断言
        response = self.login_api.get_verify_code(self.session)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))

        # 调用登录接口获取登录信息，并进行断言
        response = self.login_api.login(self.session, "13488888888", "error", "8888")
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, response.json().get("status"))
        self.assertIn("密码错误", response.json().get("msg"))