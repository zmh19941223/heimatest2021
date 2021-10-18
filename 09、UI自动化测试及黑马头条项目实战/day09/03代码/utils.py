import time

from selenium.webdriver.common.by import By
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


# 判断元素是否存
def element_is_exsit(driver, element):   # element 表示的元素定位的值
    try:  # 捕获异常信息
        get_element(driver, element)    # 能够正常找元素，就返回True
        return True
    except Exception as e:   # 如果捕获到了异常，返回False
        return False


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


# 封装滑屏操作方法
def execute_swipe(driver, fx, count=1):
    w = driver.get_window_size()["width"]  # 获取手机屏幕的宽度
    h = driver.get_window_size()["height"] # 获取手机屏幕的高度
    # w=1080  h=1920
    if fx == "top":  # 往上滑
        zb = (w/2, h*0.9, w/2, h*0.1)
        #     (540, 1728,  540, 192)
    elif fx == "down":  # 往下滑
        zb = (w/2, h*0.1, w/2, h*0.9)
    elif fx == 'left':  # 往左滑
        zb = (w*0.9, h/2, w*0.1, h/2)
    else:  # 往右滑
        zb = (w*0.1, h/2, w*0.9, h/2)
    for i in range(count):
        driver.swipe(*zb, duration=1200)
        time.sleep(1)


# 封装一个边滑动边查找的方法
def swipe_find(driver, element, element_info):  # By.XPATH, "//*[@text='存储']"
    ele_size = element.size  # 获取元素大小
    width = ele_size["width"]  # 获取元素的宽度
    height = ele_size["height"]  # 获取元素的高度
    # 获了element元素左上角点的坐标
    ele_position = element.location
    x = ele_position["x"]  # 获取左上角点的x坐标值
    y = ele_position["y"]  # 获取左上角点的y坐标值

    start_x = x + width*0.9  # 获取的是起始点X的值
    y = y + height*0.5  # 获取的是起始及终止点的Y的值
    end_x = x + width*0.1   # 获取的是终止点X的值
    while True:
        page = driver.page_source  # 记录查找前的页面资源,通过对比页面资源来退出死循环
        try:
            driver.find_element(*element_info).click()  # 如果有找到对应的元素那么点击并返回
            return True
        except Exception as e:
            print("没有找到该元素！")
        driver.swipe(start_x, y, end_x, y, duration=1000)  # 没有找到元素，那么滑屏后再对比并重新查找
        time.sleep(1)
        if page == driver.page_source:
            print("滑屏操作完成且没有找到元素信息")
            return False

# 定义获取toast消息的方法
def get_toast(driver, message, timeout=3):
    # xpath = "//*[contains(@text, '" + message + "')]"   #.format(message)   # 通过{} 符号将message当参数传到xpath表达式中去
    xpath = F"//*[contains(@text, '{message}')]"
    wait = WebDriverWait(driver, timeout, 1)
    element = wait.until(lambda x:x.find_element(By.XPATH, xpath))
    return element.text





