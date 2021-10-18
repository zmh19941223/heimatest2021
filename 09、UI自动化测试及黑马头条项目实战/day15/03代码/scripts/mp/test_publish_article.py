# 定义测试类
import pytest

from page.mp.home_page import HomeProxy
from page.mp.login_page import LoginProxy
from page.mp.publish_page import PublishProxy
from utils import UtilsDriver, is_exist


@pytest.mark.run(order=1)
class TestPublishArticle:
    # 定义类级别的fixture初始化操作方法
    def setup_class(self):
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()
        self.publish_proxy = PublishProxy()

    # 定义类级别的fixture销毁操作方法
    def teardown_class(self):
        UtilsDriver.quit_mp_driver()

    # 定义登录的测试用例
    def test_login(self):
        self.login_proxy.login("13012345678", "246810")   # 登录
        username = self.home_proxy.get_username_msg()  # 获取登录后的用户名信息
        assert "test123" == username   # 根据获取到的用户名进行断言

    # 定义测试方法
    def test_publish_article(self):
        self.home_proxy.go_publish_page()   # 跳转到发布文章页面
        self.publish_proxy.publish_article("发布文章_0710_15", "发布文章_0710_14发布文章_0710_14", "数据库")
        assert is_exist(UtilsDriver.get_mp_driver(), "新增文章成功")
