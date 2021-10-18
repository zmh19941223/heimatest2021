import time

from appium import webdriver
from selenium.webdriver.common.by import By

from utils import get_element, input_text, swipe_find

des_cap = {
"platformName" : "android" ,   #表示的是android  或者ios
"platformVersion" : "5.1.1",   #表示的是平台系统的版本号
"deviceName" : "****",    #表示的是设备的ID名称（如果只有一个设备可以用****来代替）
"appPackage" : "com.netease.newsreader.activity",   #表示app的包名
"appActivity" :  "com.netease.nr.phone.main.MainActivity",      #表示的是app的界面名
"resetKeyboard": True,        # 重置设备的输入键盘
"unicodeKeyboard": True,        # 采用unicode编码输入
"noReset": True
####"".module_main.activity.MainActivity""
}  #定义字典参数

driver = webdriver.Remote("http://localhost:4723/wd/hub",des_cap)

# 找到滑屏的元素
scroll_btn = By.ID, "com.netease.newsreader.activity:id/bn9"
scroll_element = get_element(driver, scroll_btn)

# 找到房产频道
house_btn = By.XPATH, "//*[@text='哈哈']"

# 调用封装好的边查找边滑屏的函数来找房产频道
swipe_find(driver, scroll_element, house_btn)

time.sleep(5)

driver.quit()