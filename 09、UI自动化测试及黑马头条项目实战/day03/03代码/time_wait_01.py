# 导包
import time

from selenium import  webdriver
# 实例化浏览器驱动
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)  # 隐式等待的时间，设置为5S
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 针对第一个延时框输入admin
print("开始时间：", time.strftime("%H:%M:%S"))
driver.find_element(By.XPATH, "//div[@id='wait']/input[1]").send_keys("admin")
print("找到第一个元素的时间:", time.strftime("%H:%M:%S"))
# 针对第二个延时框输入admin2
driver.find_element(By.XPATH, "//div[@id='wait']/input[2]").send_keys("admin2")
print("找到第二个元素的时间：", time.strftime("%H:%M:%S"))

# 等待3S
time.sleep(3)
# 退出浏览器驱动
driver.quit()
