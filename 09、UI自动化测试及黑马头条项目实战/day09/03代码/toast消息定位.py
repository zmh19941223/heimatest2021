import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from utils import get_element, input_text, execute_swipe, element_is_exsit, get_toast

des_cap = {
"platformName" : "android" ,   #表示的是android  或者ios
"platformVersion" : "5.1.1",   #表示的是平台系统的版本号
"deviceName" : "****",    #表示的是设备的ID名称（如果只有一个设备可以用****来代替）
"appPackage" : "com.android.settings",   #表示app的包名
"appActivity" :  ".Settings",      #表示的是app的界面名
"resetKeyboard": True,        # 重置设备的输入键盘
"unicodeKeyboard": True,        # 采用unicode编码输入
"noReset": True,
"automationName": 'Uiautomator2'
####"".module_main.activity.MainActivity""
}  #定义字典参数

driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)
# 往上滑三次
execute_swipe(driver, 'top', count=3)

# 点击关于平板电脑
about_btn = By.XPATH, "//*[@text='关于平板电脑']"
get_element(driver, about_btn).click()
time.sleep(1)
# 往上滑一次
execute_swipe(driver, 'top')

# 点击版本号
version_btn = By.XPATH, "//*[@text='版本号']"
get_element(driver, version_btn).click()
time.sleep(1)
# toast元素信息
# toast_btn = By.XPATH, "//*[contains(@text, '开发者模式')]"
print(get_toast(driver, "开发者模式"))
# driver.find_element(*toast_btn).click()
# if element_is_exsit(driver, toast_btn):
#     print("能够定位到toast消息")
# else:
#     print("不能定位到toast消息")