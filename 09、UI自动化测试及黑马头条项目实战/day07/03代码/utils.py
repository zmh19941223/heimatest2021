from selenium.webdriver.support.wait import WebDriverWait
# 定义一个获取元素的方法


# def get_element(driver, find_type, value):
#     wait = WebDriverWait(driver, 10, 1)
#     element = wait.until(lambda x: x.find_element(find_type, value))
#     return element
# 减少代码量，不必要在每个元素定位的代码中都使用显示等待来定位。
def get_element(driver, element):   # element 表示的元素定位的值
    wait = WebDriverWait(driver, 10, 1)
    element = wait.until(lambda x: x.find_element(element[0], element[1]))
    return element


#  为了保证代码的健壮性，确定输入的内容一定不会出错，所以在输入前做了一次清除。
def input_text(element, text):
    """
    :param element:  表示的是元素对象
    :param text: 表示的是要输入的内容
    :return:
    """
    # 清除元素中的文本内容
    element.clear()
    # 输入文本内容
    element.send_keys(text)
