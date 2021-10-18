import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from utils import get_element, input_text

des_cap = {
"platformName" : "android" ,   #表示的是android  或者ios
"platformVersion" : "5.1.1",   #表示的是平台系统的版本号
"deviceName" : "****",    #表示的是设备的ID名称（如果只有一个设备可以用****来代替）
"appPackage" : "com.android.settings",   #表示app的包名
"appActivity" :  ".Settings",      #表示的是app的界面名
"resetKeyboard": True,        # 重置设备的输入键盘
"unicodeKeyboard": True        # 采用unicode编码输入
####"".module_main.activity.MainActivity""
}  #定义字典参数

driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)

wlan_btn = By.XPATH, "//*[@text='WLAN']"
wlan_element = get_element(driver, wlan_btn)

# 调用轻敲手势操作
TouchAction(driver).tap(x=457, y=487).perform()
# action = TouchAction(driver)  # 创建手势对象
# # 调用手势方法
# action.tap(wlan_element)
# # 调用perform()执行
# action.perform()
time.sleep(3)
driver.quit()