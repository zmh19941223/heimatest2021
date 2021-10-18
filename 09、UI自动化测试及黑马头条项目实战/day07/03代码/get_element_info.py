# 导入webdriver
import time

from appium import webdriver
# 初始化app的配置信息
from selenium.webdriver.common.by import By

from utils import get_element

des_cap = dict()  # 定义字典参数

des_cap["platformName"] = "android"   # 表示的是android 或者IOS系统
des_cap["platformVersion"] = "5.1.1"  # 表示的是平台系统的版本号
des_cap["deviceName"] = "****"  # 表示的是设备的ID名称（如果只有一个设备可以用****来替代）
des_cap["appPackage"] = "com.android.settings"  # 表示的是app的包名
des_cap["appActivity"] = ".Settings"  # 表示的是app的界面名

driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)
# 找到wlan 元素
wlan_btn = By.ID, "com.android.settings:id/title"
element = get_element(driver, wlan_btn)
# 获取wlan菜单的文本内容
print(element.text)

# 获取wlan的位置信息
print(element.location)

# 获取wlan元素的大小
print(element.size)

# 获取wlan元素
print(element.get_attribute("className"))

time.sleep(6)

driver.quit()
