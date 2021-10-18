import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from utils import get_element, input_text

des_cap = {
"platformName" : "android" ,   #表示的是android  或者ios
"platformVersion" : "5.1.1",   #表示的是平台系统的版本号
"deviceName" : "****",    #表示的是设备的ID名称（如果只有一个设备可以用****来代替）
"appPackage" : "com.lufax.android",   #表示app的包名
"appActivity" :  ".activity.HomeActivity",      #表示的是app的界面名
"resetKeyboard": True,        # 重置设备的输入键盘
"unicodeKeyboard": True,        # 采用unicode编码输入
"noReset": True
####"".module_main.activity.MainActivity""
}  #定义字典参数

driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)

me_btn = By.XPATH, "//*[@text='我的']"
get_element(driver, me_btn).click()

TouchAction(driver).press(x=260, y=720).wait(500).move_to(x=540, y=720)\
    .wait(500).move_to(x=820,y=720).wait(500).move_to(x=540, y=1000).wait(500).move_to(x=260, y=1270)\
    .wait(500).move_to(x=540, y=1270).wait(500).move_to(x=820, y=1270).release().perform()
driver.drag_and_drop()
time.sleep(5)
driver.quit()

