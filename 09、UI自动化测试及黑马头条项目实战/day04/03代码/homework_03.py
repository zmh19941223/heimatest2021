import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://tpshop-test.itheima.net/Home/Index/index.html")

driver.find_element(By.CSS_SELECTOR, ".red").click()

# 登陆操作
driver.find_element(By.ID, "username").send_keys("13012345678")
driver.find_element(By.ID, "password").send_keys("12345678")
driver.find_element(By.ID, "verify_code").send_keys("8888")
driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()

# 通过循环的方式获取会员信息
list1 = driver.find_elements(By.CSS_SELECTOR, ".mu-afte  span")  # 返回的一组元素
list2 = driver.find_elements(By.CSS_SELECTOR, ".mu-num")  # 返回一组元素
for x in range(0, 4):
    print(list1[x].text, list2[x].text)

# 在搜索框中输入小米并进行搜索
driver.find_element(By.CSS_SELECTOR, "#q").send_keys("小米")
driver.find_element(By.CSS_SELECTOR, ".search_usercenter_btn").click()

# 将搜索到的第一个商品加入到购物车，点击关闭
driver.find_element(By.XPATH, "//*[text()='加入购物车']").click()
driver.find_element(By.CSS_SELECTOR, "#join_cart").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '.layui-layer-close').click()

# 使用悬停的方式获取购物车中的商品数量和金额， 需要进行判断，如查为空就返回购物车为空
result = driver.find_element(By.CSS_SELECTOR, "#cart_quantity").text
if result:  # result 如果为0 就是false， 如果大于0都为True
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#cart_quantity"))
    action.perform()
    time.sleep(2)
    print("商品总数：",driver.find_element(By.ID, "total_qty").text)
    print("商品总金额:", driver.find_element(By.ID, "total_pay").text)
else:
    print("购物车为空")
