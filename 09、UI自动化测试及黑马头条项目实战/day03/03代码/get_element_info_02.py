# 导包
import time
from selenium import  webdriver
# 实例化浏览器驱动
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
# 打开测试网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 4).判断页面中的span标签是否可见
print("判断元素是否可见，默认应该是False：", driver.find_element(By.NAME, "sp1").is_displayed())
# 5).判断页面中取消按钮是否可用
print("判断取消按钮是否可用，默认应该是False：", driver.find_element(By.ID, "cancelA").is_enabled())
# 6).判断页面中'旅游'对应的复选框是否为选中的状态
print("判断旅游复选框是否选中，默认应该是True:", driver.find_element(By.ID, "lyA").is_selected())
# 等待3S
time.sleep(3)
# 退出浏览器驱动
driver.quit()