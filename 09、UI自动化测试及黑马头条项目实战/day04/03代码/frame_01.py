import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
# 针对主页的用户名输入admin
driver.find_element(By.ID, "userA").send_keys("admin")

# 针对注册用户a输入用户名adminA
ele = driver.find_element(By.ID, "idframe1")
driver.switch_to.frame(ele)
driver.find_element(By.ID, "AuserA").send_keys("adminA")

# 回到默认首页面
driver.switch_to.default_content()

# 针对注册用户B输入用户名adminB
ele_frame = driver.find_element(By.ID, "idframe2")
driver.switch_to.frame(ele_frame)
driver.find_element(By.ID, "BuserA").send_keys("adminB")

time.sleep(3)


driver.quit()