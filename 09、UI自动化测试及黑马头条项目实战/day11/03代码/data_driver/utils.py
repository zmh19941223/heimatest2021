# 定义一个工具类
import json
import time

from selenium import webdriver


from selenium.webdriver.common.by import By


class UtilsDriver:
    _driver = None

    # 定义一个获取浏览器驱动对象的方法
    @classmethod   # 表示这个方法是一个类级别的方法
    def get_driver(cls):
        if cls._driver is None:  # 判断driver是否已创建，如果为None就需要去创建浏览器驱动对象，如果不为None，则直接返回driver
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
            cls._driver.get("http://tpshop-test.itheima.net/")
        return cls._driver

    # 定义一个退出浏览器驱动对象的方法  浏览器驱动对象退出之后，还有一串效的字符串存在
    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls.get_driver().quit()
            cls._driver = None


# 定义一个获取弹出框消息的方法
def get_msg():
    time.sleep(1)
    # driver = UtilsDriver()
    return UtilsDriver.get_driver().find_element(By.CSS_SELECTOR, ".layui-layer-content").text


def get_case_data(filename):
    with open(filename, encoding='utf-8') as f:
        case_data = json.load(f)
    list_case_data = []
    for case in case_data:
        for x in case.values():  # values() 用来获取字典对象里面的键值
            case_tuple = x.values()
            list_case_data.append(tuple(case_tuple))
    return list_case_data
# get_case_data("case_data/login_case_data.json")


def case_data(filename):
    with open(filename, encoding='utf-8') as f:
        case_data = json.load(f)
    list_case_data = []
    for case in case_data.values():
        list_case_data.append(tuple(case.values()))
    return list_case_data



# case_data("case_data/login_case_data.json")