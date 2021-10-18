# 导包selenium
import time

from selenium import webdriver
# 创建浏览器驱动对象
driver = webdriver.Chrome()
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 通过ID定位到用户名输入框并在用户名输入框中输入admin
driver.find_element_by_id("userA").send_keys("admin")
# 通过ID定位到密码输入框并在密码输入框中输入123456
driver.find_element_by_id("passwordA").send_keys("123456")
# 等待3s
time.sleep(3)
# 退出浏览器
driver.quit()

