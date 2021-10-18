from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 创建浏览器驱动对象
driver.maximize_window()
driver.implicitly_wait(10)

# 打开topshop首页
driver.get("http://tpshop-test.itheima.net/")
# 点击登陆跳转到登录页面
driver.find_element(By.CSS_SELECTOR, ".red").click()
# 输入用户名、密码、验证码
driver.find_element(By.ID, "username").send_keys("13012345678")
driver.find_element(By.ID, "password").send_keys("12345678")
driver.find_element(By.ID, "verify_code").send_keys("8888")

# 点击登录按钮
driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()

# 点击首页返回到topshop首页面
driver.find_element(By.XPATH, "//*[text()='首页']").click()

# 找到首页中的第一个产品点击并加入到购物车
driver.find_element(By.XPATH,"//*[@class='floor-goods-list']/a[1]").click()
driver.find_element(By.XPATH, "//*[text()='加入购物车']").click()

# 点击继续购物
# 切换到继续购物的iframe中
driver.switch_to.frame(driver.find_element(By.ID, "layui-layer-iframe1"))
driver.find_element(By.XPATH, "//*[text()='继续购物']").click()

# 点击我的订单
driver.find_element(By.XPATH, "//*[text()='我的订单']").click()
# 点击我的订单之后需要做窗口切换
driver.switch_to.window(driver.window_handles[-1])

# 点击待付款
driver.find_element(By.XPATH, "//*[text()='待付款']").click()

# 点击第一个订单的立即支付
driver.find_element(By.CSS_SELECTOR, ".ps_lj").click()

# 需要再一次窗口切换
driver.switch_to.window(driver.window_handles[-1])

# 选择支付方式
driver.find_element(By.CSS_SELECTOR, "[value='pay_code=cod']").click()

# 确认支付方式
driver.find_element(By.CSS_SELECTOR, ".button-confirm-payment").click()

