# 导包
import time
from selenium import webdriver
# 创建浏览器驱动对象
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 1).通过脚本执行输入用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com
driver.find_element(By.ID, "userA").send_keys("admin")
driver.find_element(By.ID, "passwordA").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".telA").send_keys("18611111111")
driver.find_element(By.XPATH, "//*[@class='emailA dzyxA']").send_keys("123@qq.com")
# 2).间隔3秒，修改电话号码为：18600000000
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".telA").clear()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".telA").send_keys("18600000000")

# 等待3S
time.sleep(3)
# 退出
driver.quit()
