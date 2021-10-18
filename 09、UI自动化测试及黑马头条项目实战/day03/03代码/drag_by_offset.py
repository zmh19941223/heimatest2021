# 导包
import time

from selenium import  webdriver
# 实例化浏览器驱动
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E9%AA%8C%E8%AF%81%E7%A0%81/index.html")

# 模拟鼠标实现滑块验证码的操作
element = driver.find_element(By.CSS_SELECTOR, '.handler_bg')
# 创建鼠标对象
action = ActionChains(driver)
# 调用鼠标单元素拖动事件方法
action.drag_and_drop_by_offset(element, 265, 0)
# 调用鼠标执行方法
action.perform()

# 等待3S
time.sleep(3)
# 退出浏览器驱动
driver.quit()