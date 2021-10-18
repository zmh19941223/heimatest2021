import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from utils import get_element, input_text, execute_swipe, element_is_exsit, get_toast

des_cap = {
"platformName" : "android" ,   #表示的是android  或者ios
"platformVersion" : "5.1.1",   #表示的是平台系统的版本号
"deviceName" : "****",    #表示的是设备的ID名称（如果只有一个设备可以用****来代替）
"appPackage" : "com.android.browser",   #表示app的包名
"appActivity" :  ".BrowserActivity",      #表示的是app的界面名
"resetKeyboard": True,        # 重置设备的输入键盘
"unicodeKeyboard": True,        # 采用unicode编码输入
"noReset": True,
"automationName": 'Uiautomator2',
"chromedriverExecutableDir": r"D:\BaiduNetdiskDownload\apptools\apk\chromedriver_win32_2.22"  # 用来指定chrome驱动的目录
####"".module_main.activity.MainActivity""
}  #定义字典参数

driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)

print(driver.contexts)
driver.get("http://m.baidu.com")
time.sleep(2)
driver.switch_to.context("WEBVIEW_com.android.browser")

driver.find_element(By.ID, "index-kw").send_keys("python")
time.sleep(3)
driver.find_element(By.ID, "index-bn").click()
time.sleep(5)
driver.quit()
