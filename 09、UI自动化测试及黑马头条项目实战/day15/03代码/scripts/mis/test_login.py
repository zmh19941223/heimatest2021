# 定义测试类
import pytest

from page.mis.home_page import HomeProxy
from page.mis.login_page import LoginProxy
from utils import UtilsDriver


@pytest.mark.run(order=1001)
class TestLogin:
    # 定义类级别的fixture初始化操作
    def setup_class(self):
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()

    # 定义类级别的fixture销毁操作
    def teardown_class(self):
        UtilsDriver.quit_mis_driver()

    # 定义测试方法
    def test_login(self):
        """
        测试数据： 用户名：testid   密码:testpwd123
        :return:
        """
        self.login_proxy.login("testid", "testpwd123")
        result = self.home_proxy.get_user()
        assert "管理员" in result
