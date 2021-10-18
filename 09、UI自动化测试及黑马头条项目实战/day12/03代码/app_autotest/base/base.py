# 定义对象库层的基类
from selenium.webdriver.support.wait import WebDriverWait

from app_autotest.utils import UtilsDriver


class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_app_driver()

    # 定义获取元素对象的方法
    def get_element(self, location):
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*location))
        return element


# 定义操作层的基类
class BaseHandle:
    # 输入元素的内容的方法
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)
