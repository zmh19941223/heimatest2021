# 导包
import time
from selenium import webdriver
# 创建浏览器驱动对象
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")

# 通过css的层级选择器定位用户名输入框输入admin
# driver.find_element_by_css_selector(".zc #userA").send_keys("admin")
driver.find_element_by_css_selector(".zc #userA").send_keys("admin")
# driver.find_element(By.ID, "userA")
# driver.find_element(By.XPATH, "//*[@id='userA']")
# 等待3S
time.sleep(3)
# 退出
driver.quit()


