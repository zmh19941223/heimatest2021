#导入模块
import time
from selenium import webdriver
#浏览器驱动实例化
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#窗口最大化
driver.maximize_window()
#打开测试网站
driver.get("http://tpshop-test.itheima.net/")
#进入tpshop首页并点击登录
driver.find_element_by_link_text("登录").click()
#清空原有信息并重新输入
driver.find_element_by_css_selector("#username").clear()
driver.find_element_by_css_selector("#username").send_keys("13012345678")
driver.find_element_by_name("password").send_keys("12345678")
driver.find_element_by_css_selector("#verify_code").send_keys("8888")
driver.find_element(By.CSS_SELECTOR,".J-login-submit").click()
time.sleep(5)
#循环打印会员首页的会员折扣、可用积分、账户余额、优惠券信息
elements = driver.find_elements(By.CSS_SELECTOR,".mu-num")
time.sleep(5)
print(elements)
print(elements[0].text)