#导包
import time
from selenium import webdriver
#实例化浏览器驱动
driver = webdriver.Chrome
#打开CSDN官方网站
driver.get("https://www.csdn.net/")
#通过Xpath的绝对路径定位CSDN的网站首页左侧推荐列表中的“前端”
driver.find_element_by_xpath("/html/body/div/nav/div/div/ul/li[7]/a").send_keys("前端")
time.sleep(4)
driver.quit()