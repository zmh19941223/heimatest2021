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
"appPackage" : "com.bjcsxq.chat.carfriend",   #表示app的包名
"appActivity" :  ".module_main.activity.SplashActivity",      #表示的是app的界面名
"noReset": True  # 用来记住app的session，如果有登陆或做过初始化的操作，为True时，后面不需要再操作
####"".module_main.activity.MainActivity""
}  #定义字典参数

driver = webdriver.Remote("http://localhost:4723/wd/hub",des_cap)

agree_btn = By.XPATH, "//*[@text='同意并继续使用APP']"

# 通过同意协议来判断app是否是首次打开
if element_is_exsit(driver, agree_btn):
    get_element(driver, agree_btn).click()
else:
    print("非首次打开")

# 点击“我的”
me_element = By.ID,"com.bjcsxq.chat.carfriend:id/mine_layout"
get_element(driver, me_element).click()
# 登录
login_element = By.ID, "com.bjcsxq.chat.carfriend:id/mine_username_tv"
get_element(driver, login_element).click()
# 输入手机号
tel_element = By.ID, "com.bjcsxq.chat.carfriend:id/login_phone_et"
input_text(get_element(driver, tel_element), "13751113926")
# 输入密码
password_element = By.ID, "com.bjcsxq.chat.carfriend:id/login_pwd_et"
input_text(get_element(driver, password_element), "a123456b")
# 点击登录
insert_element = By.ID, "com.bjcsxq.chat.carfriend:id/login_btn"
get_element(driver, insert_element).click()
# 点击确定
accept_element = By.CLASS_NAME, "android.widget.Button"
get_element(driver, accept_element).click()
# 点击“驾照圈”
licence_btn = By.ID, "com.bjcsxq.chat.carfriend:id/apply_layout"
get_element(driver, licence_btn).click()
# 选择第一条评论
pl_element = By.ID, "com.bjcsxq.chat.carfriend:id/tv_post_replay"
get_element(driver, pl_element).click()
# 填写评论内容
nr_element = By.XPATH, "//*[@text='发布评论']"
input_text(get_element(driver, nr_element), "test")
# 进行发布
fb_element = By.CLASS_NAME, "android.widget.TextView"
get_element(driver, fb_element)
time.sleep(3)
driver.quit()
