from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


# 可以通过 driver.switch_to.frame(frame_element) # frame_element表示的是元素对象
ele = driver.find_element(By.ID, "layui-layer2")
driver.switch_to.frame(ele)

# 可以通过driver.switch_to.default_content() 方法回到默认首页
driver.switch_to.default_content()
