import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 手动登出获取登出之后的cookie信息
cookie = {
    "name": "BDUSS",
    "value": "kU5SWFZZEJHWHRSMUx2dkxiR3Zmcm4yV2RUV2pXLWkxci1jUklDTG8tUkExSzllRVFBQUFBJCQAAAAAAAAAAAEAAAD6Amsqwc63yXp6egAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEBHiF5AR4heW"
}
# 在浏览器中添加cookie信息
driver.add_cookie(cookie)

# 页面刷新
driver.refresh()

time.sleep(3)

