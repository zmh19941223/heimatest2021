# 定义一个对象库层的基类
from selenium.webdriver.support.wait import WebDriverWait

from data_driver.utils import UtilsDriver


class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_driver()

    # 定义获取元素对象的方法
    def get_element(self, location):
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*location))
        return element


# 定义操作层的基类
class BaseHandle:
    # 定义针对元素的输入操作方法
    def input_text(self, element, text):
        """
        :param element: 表示的是元素对象
        :param text:  表示的是要输入的内容
        :return:
        """
        element.clear()
        element.send_keys(text)
