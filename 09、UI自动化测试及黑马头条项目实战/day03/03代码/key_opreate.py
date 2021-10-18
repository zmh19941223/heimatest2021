# 导包
import time

from selenium import  webdriver
# 实例化浏览器驱动
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 1). 输入用户名：admin1，暂停2秒，删除1
element = driver.find_element(By.ID, 'userA')
element.send_keys("admin1")
time.sleep(2)
element.send_keys(Keys.BACK_SPACE)  # 删除最后一个字符串 clear()
# 2). 全选用户名：admin，暂停2秒
element.send_keys(Keys.CONTROL, 'a')
time.sleep(2)
# 3). 复制用户名：admin，暂停2秒
element.send_keys(Keys.CONTROL, 'c')
time.sleep(2)
# 4). 粘贴到密码框
driver.find_element(By.ID, 'passwordA').send_keys(Keys.CONTROL, 'V')

# 等待3S
time.sleep(3)
# 退出浏览器驱动
driver.quit()
