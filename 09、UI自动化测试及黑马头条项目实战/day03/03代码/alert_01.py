# 导包
import time

from selenium import  webdriver
# 实例化浏览器驱动
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 点击alert按钮
driver.find_element(By.ID, "alerta").click()
time.sleep(3)
# 处理弹出框
# 获取弹出框
alert = driver.switch_to.alert
# 打印信息，然后取消
print(alert.text)
alert.dismiss()
# 在用户名输入框中输入admin
driver.find_element(By.ID, 'userA').send_keys("admin")

# 等待3S
time.sleep(3)
# 退出浏览器驱动
driver.quit()