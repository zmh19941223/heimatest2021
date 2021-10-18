import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")
# try:
    # 输入用户名
driver.find_element(By.ID, "userA").send_keys("admin")

# 输入密码
#     driver.find_element(By.ID, "padd").send_keys("1234")
# except Exception as e:
driver.get_screenshot_as_file("img/error.png")
    # raise e

time.sleep(3)
driver.quit()
