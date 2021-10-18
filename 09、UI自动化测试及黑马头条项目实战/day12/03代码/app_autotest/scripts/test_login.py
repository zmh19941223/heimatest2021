import pytest

from app_autotest.page.home_page import HomeProxy
from app_autotest.page.login_page import LoginProxy
from app_autotest.page.mine_page import MineProxy
from app_autotest.utils import UtilsDriver


class TestLogin:
    # 定义fixture初始化操作
    def setup_class(self):
        self.home_proxy = HomeProxy()
        self.mine_proxy = MineProxy()
        self.login_proxy =LoginProxy()
        self.home_proxy.go_me_page()  # 跳转到我的页面
        self.mine_proxy.go_login_page()  # 跳转到登录页面

    # 定义fixture销毁操作
    def teardown_class(self):
        UtilsDriver.quit_app_driver()

    @pytest.mark.parametrize("mobile, password, expect",
                             [("1388888888", "123456", "账号还未注册"),
                              ("13751113926", "123678", "账号或密码错误")])
    def test_login_01(self, mobile, password, expect):
        self.login_proxy.login(mobile, password)
        result = self.login_proxy.get_tip_msg()
        assert expect in result

