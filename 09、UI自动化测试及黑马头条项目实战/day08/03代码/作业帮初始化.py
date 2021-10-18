# 导入webdriver
import time
from appium import webdriver
# 初始化app的配置信息
from selenium.webdriver.common.by import By

from utils import get_element, input_text, element_is_exsit

des_cap = {
"platformName" : "android" ,   #表示的是android  或者ios
"platformVersion" : "5.1.1",   #表示的是平台系统的版本号
"deviceName" : "****",    #表示的是设备的ID名称（如果只有一个设备可以用****来代替）
"appPackage" : "com.baidu.homework",   #表示app的包名
"appActivity" :  ".activity.init.InitActivity",      #表示的是app的界面名
"noReset": True  # 用来记住app的session，如果有登陆或做过初始化的操作，为True时，后面不需要再操作
####"".module_main.activity.MainActivity""
}  #定义字典参数

driver = webdriver.Remote("http://localhost:4723/wd/hub",des_cap)

skip_btn = By.XPATH, "//*[@text='跳过']"
time.sleep(5)
if element_is_exsit(driver, skip_btn):
    get_element(driver, skip_btn).click()

    student_btn = By.XPATH, "//*[@text='学生']"
    get_element(driver, student_btn).click()

    class_btn = By.XPATH, "//*[@text='一年级']"
    get_element(driver, class_btn).click()

    finish_btn = By.XPATH, "//*[@text='完成']"
    get_element(driver, finish_btn).click()

    id_btn = By.ID, "com.baidu.homework:id/dialog_guide_view"
    get_element(driver, id_btn).click()
    time.sleep(1)
    get_element(driver, id_btn).click()
    time.sleep(1)
    get_element(driver, id_btn).click()
else:
    print("是非首次打开！")