# 导包
import time
from selenium import  webdriver
# 实例化浏览器驱动
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")

# 输入用户名admin，暂停3秒钟后，双击鼠标左键，选中admin
element = driver.find_element(By.ID, "userA")
element.send_keys("admin")
time.sleep(3)
# 创建鼠标对象
action = ActionChains(driver)
# 调用鼠标双击事件方法
action.double_click(element)
# 调用鼠标执行方法
action.perform()

# 等待3S
time.sleep(3)
# 退出浏览器驱动
driver.quit()