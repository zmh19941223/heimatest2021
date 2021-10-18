import time

from appium import webdriver
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
# 存储
save_btn = By.XPATH, "//*[@text='存储']"
# 更多
more_btn = By.XPATH, "//*[@text='更多']"

# 通过拖动来实现滑屏操作
driver.drag_and_drop(get_element(driver, save_btn),  get_element(driver, more_btn))

time.sleep(3)

driver.quit()