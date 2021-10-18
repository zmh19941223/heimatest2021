# 导包
import time
from selenium import webdriver
# 创建浏览器驱动对象
driver = webdriver.Chrome()
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 通过xpath的绝对路径定位用户名输入框并输入admin
driver.find_element_by_xpath("/html/body/div/fieldset/form/p/input").send_keys("admin")
# 等待3S
time.sleep(3)
# 通过xapth的相对路径定位密码输入框并输入123
driver.find_element_by_xpath("//form/p[2]/input").send_keys("123")
# 等待3S
time.sleep(3)
# 退出
driver.quit()
