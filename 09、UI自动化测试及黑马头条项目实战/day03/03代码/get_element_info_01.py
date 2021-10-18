# 导包
import time

from selenium import  webdriver
# 实例化浏览器驱动
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 1).获取用户名输入框的大小
print(driver.find_element(By.ID, "userA").size)
# 2).获取页面上第一个超链接的文本内容
print(driver.find_element(By.LINK_TEXT, "新浪").text)
# 3).获取页面上第一个超链接的地址
print(driver.find_element(By.LINK_TEXT, "新浪").get_attribute("href"))
# 等待3S
time.sleep(3)
# 退出浏览器驱动
driver.quit()