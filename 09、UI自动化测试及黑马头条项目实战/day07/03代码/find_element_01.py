# 导入webdriver
import time

from appium import webdriver
# 初始化app的配置信息
from selenium.webdriver.common.by import By

des_cap = dict()  # 定义字典参数

des_cap["platformName"] = "android"   # 表示的是android 或者IOS系统
des_cap["platformVersion"] = "5.1.1"  # 表示的是平台系统的版本号
des_cap["deviceName"] = "****"  # 表示的是设备的ID名称（如果只有一个设备可以用****来替代）
des_cap["appPackage"] = "com.android.settings"  # 表示的是app的包名
des_cap["appActivity"] = ".Settings"  # 表示的是app的界面名

driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)
# 找到“更多”按钮并点击(XPATH)
element = driver.find_element(By.XPATH, "//*[@text='更多']")
element.click()
time.sleep(2)
# 找到 飞行模式的 开关，并点击(ID)
air_element = driver.find_element(By.ID, "android:id/switchWidget")
air_element.click()
time.sleep(2)
# 找到返回按钮并点击(class)
return_element = driver.find_element(By.CLASS_NAME, "android.widget.ImageButton")
return_element.click()
time.sleep(3)
driver.quit()
