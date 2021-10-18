# 定义测试类
import time

import pytest

from page.mis.audit_page import AuditProxy
from page.mis.home_page import HomeProxy
from utils import UtilsDriver


@pytest.mark.run(order=1002)
class TestAuditArticle:
    # 定义类级别的fixture初始化操作
    def setup_class(self):
        self.home_proxy = HomeProxy()
        self.audit_proxy = AuditProxy()

    # 定义类级别的fixture销毁操作
    def teardown_class(self):
        UtilsDriver.quit_mis_driver()

    # 定义测试方法
    def test_audit_article(self):
        time.sleep(1)
        self.home_proxy.go_content_audit()
        self.audit_proxy.audit_article("发布文章_0828_15", "待审核", "2020-09-13 22:00:00")
        result = self.audit_proxy.audit_article_pass("发布文章_0828_15")
        assert result

        # 如果值为0， 为None， 为False， 判断时反回的都是false
        # 其他任何的值判断时都是为True
