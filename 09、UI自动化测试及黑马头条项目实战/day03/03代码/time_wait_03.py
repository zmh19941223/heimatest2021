# 导包
import time

from selenium import  webdriver
# 实例化浏览器驱动
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://tpshop-test.itheima.net/")

# 先登录
driver.find_element(By.CSS_SELECTOR, '.red').click()
# 输入用户名密码等信息
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("13012345678")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("12345678")
driver.find_element(By.CSS_SELECTOR, "#verify_code").send_keys("8888")
driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()

# 获取购物车中的商品数量
time.sleep(2)
print("购物车商品数量:", driver.find_element(By.CSS_SELECTOR, "#cart_quantity").text)

# 等待3S
time.sleep(3)
# 退出浏览器驱动
driver.quit()
