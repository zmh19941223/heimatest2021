import time

from selenium import webdriver
driver=webdriver.Chrome()


driver.get("http://www.baidu.com")
# 打印所有cookie信息
print(driver.get_cookies())

# 获取单个cookie信息
print(driver.get_cookie("BAIDUID"))

# 往百度中添加一个cookie
cookie_dict = {
    "name":"test_baidu",
    "value":"test_value"
}
driver.add_cookie(cookie_dict)
print("----------------------------------------------")
print(driver.get_cookies())
time.sleep(2)
driver.quit()