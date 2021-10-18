# 导包
import time

from selenium import  webdriver
# 实例化浏览器驱动
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")
element = driver.find_element(By.CSS_SELECTOR, "#selectA")
select = Select(element)
# 通过select对象的index来选择广州
time.sleep(2)
select.select_by_index(2)
# 通过select对象的value来选择上海
time.sleep(2)
select.select_by_value("sh")
# 通过select对象的visible来选择深圳
time.sleep(2)
select.select_by_visible_text("深圳")

# 等待3S
time.sleep(3)
# 退出浏览器驱动
driver.quit()