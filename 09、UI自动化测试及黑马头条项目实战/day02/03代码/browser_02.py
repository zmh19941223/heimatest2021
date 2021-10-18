import time

from selenium import webdriver
# 创建浏览器驱动对象
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 在注册A页面中点击 新浪网站
driver.find_element(By.CSS_SELECTOR, "#linkto>a").click()
# 调用浏览器的后退
time.sleep(3)
driver.back()
# 再调用浏览器的前进
time.sleep(3)
driver.forward()
# 再调用浏览器的后退
time.sleep(3)
driver.back()
# 点击击访问新浪网站
driver.find_element(By.XPATH, "//*[text()='访问 新浪 网站']").click()
time.sleep(3)
# 再调用关闭按钮
driver.close()
time.sleep(3)
# 等待3S
time.sleep(3)
# 退出
driver.quit()