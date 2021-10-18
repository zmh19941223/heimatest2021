import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 定义获取手机号码的函数名
def get_mobile():
    mobiles = ['130', '131', '134', '135']  # 确定手机号码所需要格式
    number = str(int(time.time()))[2:]  # 通过时间戳获取手机号码的后8位数(一定不会重复)
    mobile = random.choice(mobiles)+number  # 把手机号码格式的三位数与后8位数相加
    return mobile


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://tpshop-test.itheima.net/Home/user/reg.html")

driver.find_element(By.ID,  "username").send_keys(get_mobile())
driver.find_element(By.NAME,  "verify_code").send_keys("8888")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "password2").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".J_btn_agree").click()
time.sleep(10)
driver.quit()