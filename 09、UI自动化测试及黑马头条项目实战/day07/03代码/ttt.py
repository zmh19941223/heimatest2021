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
des_cap["appPackage"] = "com.baidu.homework"  # 表示的是app的包名
des_cap["appActivity"] = ".activity.user.passport.ChoiceLoginModeActivity"  # 表示的是app的界面名
des_cap["noReset"] = False
driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)
skip_btn = By.XPATH, "//*[@text='跳过']"
get_element(driver, skip_btn).click()

student_btn = By.XPATH, "//*[@text='学生']"
get_element(driver, student_btn)

class_btn = By.XPATH, "//*[@text='一年级']"
time.sleep(6)

driver.quit()