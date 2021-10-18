# 定义测试类
import pytest

from page.app.index_page import IndexProxy
from utils import UtilsDriver


@pytest.mark.run(order=2000)
class TestFindChannel:
    # 定义类级别的fixture初始化方法
    def setup_class(self):
        self.indxe_proxy = IndexProxy()

    # 定义类级别的fixture销毁方法
    def teardown_class(self):
        UtilsDriver.quit_app_driver()

    # # 定义测试方法
    # def test_find_channel(self):
    #     self.indxe_proxy.find_channel("数据库")
