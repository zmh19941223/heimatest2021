import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://tpshop-test.itheima.net/")
print(driver.get_cookies())
# 手动登出获取登出之后的cookie信息
dict1 = {"name":"user_id", "value":"2594"}
dict2 = {"name":"uname",  "value":"13012345678"}
# 在浏览器中添加cookie信息
driver.add_cookie(dict1)
driver.add_cookie(dict2)
# 页面刷新
driver.refresh()

print(driver.get_cookies())
time.sleep(3)

# [{'domain': 'localhost', 'httpOnly': False, 'name': 'uname', 'path': '/', 'secure': False, 'value': '13262728888'},
#  {'domain': 'localhost', 'httpOnly': False, 'name': 'user_id', 'path': '/', 'secure': False, 'value': '2593'},
#  {'domain': 'localhost', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'p9lb30gdb7p17nc1ngurdproc2'},
#  {'domain': 'localhost', 'expiry': 1593181147, 'httpOnly': False, 'name': 'is_mobile', 'path': '/', 'secure': False, 'value': '0'}]


[{'domain': 'localhost', 'httpOnly': False, 'name': 'uname', 'path': '/', 'secure': False, 'value': '13262728888'},
 {'domain': 'localhost', 'httpOnly': False, 'name': 'user_id', 'path': '/', 'secure': False, 'value': '2593'},
 {'domain': 'localhost', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'sn8brd3ghnu898joop305d97u0'},
 {'domain': 'localhost', 'expiry': 1593181457, 'httpOnly': False, 'name': 'is_mobile', 'path': '/', 'secure': False, 'value': '0'}]