# 定义内容审核页面对象
import time

from selenium.webdriver.common.by import By

from base.mis.base import BasePage, BaseHandle

# 定义对象库层
from utils import UtilsDriver, choice_channel, is_exist


class AuditPage(BasePage):
    def __init__(self):
        super().__init__()
        # 文章标题
        self.title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
        # 状态选择
        self.channel = By.CSS_SELECTOR, "[placeholder='请选择状态']"
        # 查询按钮
        self.query_btn = By.CSS_SELECTOR, ".find"
        # 通过按钮
        self.pass_btn = By.XPATH, "//tbody/tr/td[8]/div/button[2]"
        # 确定按钮
        self.confirm_btn = By.CSS_SELECTOR, ".el-button--primary"
        # 结束时间
        self.end_time = By.XPATH, "//*[@placeholder='选择结束时间']"

    # 定位文章标题
    def find_title(self):
        return self.get_element(self.title)

    # 定位状态选择框
    def find_channel(self):
        return self.get_element(self.channel)

    # 定位查询按钮
    def find_query_btn(self):
        return self.get_element(self.query_btn)

    # 定位通过按钮
    def find_pass_btn(self):
        return self.get_element(self.pass_btn)

    # 定位确定按钮
    def find_confirm_btn(self):
        return self.get_element(self.confirm_btn)

    # 输入结束时间
    def find_end_time(self):
        return self.get_element(self.end_time)


# 定义操作层
class AuditHandle(BaseHandle):
    def __init__(self):
        self.audit_page = AuditPage()

    # 输入文章标题
    def input_title(self, title):
        self.input_text(self.audit_page.find_title(), title)

    # 选择状态
    def choice_status(self, status):
        choice_channel(self.audit_page.driver, self.audit_page.find_channel(), status)

    # 输入结束时间
    def input_end_time(self, end_time):
        self.input_text(self.audit_page.find_end_time(), end_time)

    # 点击查询
    def click_query_btn(self):
        self.audit_page.find_query_btn().click()

    # 点击通过
    def click_pass_btn(self):
        self.audit_page.find_pass_btn().click()

    # 点击确定
    def click_confirm_btn(self):
        self.audit_page.find_confirm_btn().click()


# 定义业务层
class AuditProxy:
    def __init__(self):
        self.audit_handle = AuditHandle()
        self.driver = UtilsDriver.get_mis_driver()

    # 审核第一条文章
    def audit_article(self, title, status, end_time):
        self.audit_handle.input_title(title)  # 输入文章标题
        self.audit_handle.choice_status(status)  # 选择文章的状态
        self.audit_handle.input_end_time(end_time)  # 输入结束时间
        time.sleep(1)
        self.audit_handle.click_query_btn()  # 点击查询按钮
        time.sleep(1)
        self.audit_handle.click_pass_btn()  # 点击第一条文章的通过按钮
        time.sleep(1)
        self.audit_handle.click_confirm_btn()  # 点击确认按钮

    # 查询审核通过
    def audit_article_pass(self, title):
        self.audit_handle.input_title(title)
        time.sleep(1)
        self.audit_handle.choice_status("审核通过")
        time.sleep(1)
        self.audit_handle.click_query_btn()
        time.sleep(1)
        return is_exist(self.driver, title)
