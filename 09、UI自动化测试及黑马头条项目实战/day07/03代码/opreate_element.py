# 导入webdriver
import time

from appium import webdriver
# 初始化app的配置信息
from selenium.webdriver.common.by import By

from utils import get_element, input_text

des_cap = dict()  # 定义字典参数

des_cap["platformName"] = "android"   # 表示的是android 或者IOS系统
des_cap["platformVersion"] = "5.1.1"  # 表示的是平台系统的版本号
des_cap["deviceName"] = "****"  # 表示的是设备的ID名称（如果只有一个设备可以用****来替代）
des_cap["appPackage"] = "com.android.settings"  # 表示的是app的包名
des_cap["appActivity"] = ".Settings"  # 表示的是app的界面名

driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)
#  在设置 点击 搜索按钮
search_btn = By.ID, "com.android.settings:id/search"
get_element(driver, search_btn).click()
time.sleep(3)
#  在搜索框中输入 WIFI
input_element = By.ID, "android:id/search_src_text"
# get_element(driver, input_element).send_keys("WIFI")
input_text(get_element(driver, input_element), "WIFI")
time.sleep(3)
#  在搜索框中清除输入的内容
get_element(driver, input_element).clear()
time.sleep(3)
#  点击返回
return_btn = By.CLASS_NAME, "android.widget.ImageButton"
get_element(driver, return_btn).click()

time.sleep(3)

driver.quit()