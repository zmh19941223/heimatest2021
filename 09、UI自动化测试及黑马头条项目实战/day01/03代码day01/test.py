import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/index.php/Home/user/reg.html")
driver.find_element_by_link_text("注册").click()
driver.find_element_by_name("username").send_keys("13632909780")
driver.find_element_by_name("verify_code").send_keys("8888")
driver.find_element_by_id("password").send_keys("chenyuecong")
driver.find_element_by_id("password2").send_keys("chenyuecong")
driver.find_element_by_name("invite").send_keys("18822864704")
driver.find_element_by_link_text("同意协议并注册").click()
time.sleep(3)
driver.quit()