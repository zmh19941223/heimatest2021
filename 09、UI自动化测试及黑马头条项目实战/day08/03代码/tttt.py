from appium import webdriver
import time
from utils import element_is_exsit
from selenium.webdriver.common.by import By

from utils import *
des_cap = {
    "platformName": "android",
    "platformVersion": "5.1.1",
    "deviceName": "emulator-5554",
    "appPackage": "com.baidu.homework",
    "appActivity": ".activity.init.InitActivity",
    "noReset": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",des_cap)
time.sleep(5)
skip_element = By.XPATH,"//*[@text = '跳过']"
if element_is_exsit(driver,skip_element):
    get_element(driver,skip_element).click()
else:
    print("作业帮不是首次打开,不需要初始化操作")
time.sleep(3)
driver.quit()