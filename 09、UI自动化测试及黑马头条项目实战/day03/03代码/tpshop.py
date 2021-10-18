import time
from  selenium  import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
# 1.进入tpshop首页并登陆
driver.get("http://tpshop-test.itheima.net/")
driver.find_element(By.CSS_SELECTOR,".red").click()
driver.find_element_by_xpath("//*[contains(@autofocus,'autofocus')]").send_keys("13012345678")
driver.find_element_by_xpath("//div/input[@class='text_cmu' and @name = 'password']").send_keys("12345678")
driver.find_element_by_xpath("//input[@name='verify_code']").send_keys("8888")
driver.find_element_by_xpath("//a[@class='J-login-submit']").click()
time.sleep(3)

# 2.循环打印会员首页的会员折扣、可用积分、账户余额、优惠券信息
list1 = driver.find_elements_by_xpath("//*[@class='mu-afte fl']/ul/li/a/span")
list2 = driver.find_elements_by_xpath("//*[@class='mu-afte fl']/ul/li/a/em[@class = 'mu-num']")
for a in range(0,4):
    print(list1[a].text,list2[a].text)
# 3.在会员首页顶部的搜索引擎中输入小米，点击搜索
driver.find_element(By.CSS_SELECTOR,"input#q").send_keys("小米")
driver.find_element(By.XPATH,"//*[@class = 'search_usercenter_btn']").click()

# 4.将第一个搜索到的数据结果加入到购物车,点击关闭按钮
driver.find_element(By.LINK_TEXT,"加入购物车").click()
print("dian ji jia ru gou che:", time.strftime("%H:%M:%S"))
driver.find_element(By.CSS_SELECTOR,"#join_cart").click()
# time.sleep(3)
element_close=WebDriverWait(driver, 10, 1).until(lambda x:x.find_element(By.XPATH,"//*[@class='layui-layer-ico layui-layer-close layui-layer-close1']"))
# driver.find_element(By.XPATH,"//*[@class='layui-layer-ico layui-layer-close layui-layer-close1']").click()
element_close.click()
print("dian ji close:", time.strftime("%H:%M:%S"))
time.sleep(3)
# 5.到购物车的中获取商品数量以及总金额，需要用到判断条件，判断是否为空
action = ActionChains(driver)
element =driver.find_element(By.XPATH,"//*[@class='c-n fl']/span")
action.move_to_element(element)
action.perform()
time.sleep(3)
num1 = driver.find_element(By.XPATH,"//*[@id = 'total_qty']").text
price1 = driver.find_element(By.XPATH,"//*[@id = 'total_pay']").text
if num1 == 0:
    print("购物车为空")
else:
    print("购物车里有%s件商品，总金额为%s"%(num1,price1))
time.sleep(3)

driver.quit()