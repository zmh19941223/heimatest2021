# 导入webdriver
import time

from appium import webdriver
# 初始化app的配置信息
des_cap = {   # 定义字典参数
    "platformName": "android",   # 表示的是android 或者IOS系统
    "platformVersion": "5.1.1",  # 表示的是平台系统的版本号
    "deviceName": "****",  # 表示的是设备的ID名称（如果只有一个设备可以用****来替代）
    "appPackage": "com.android.settings",  # 表示的是app的包名
    "appActivity": ".Settings"  # 表示的是app的界面名
    }

driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)
time.sleep(2)

driver.start_activity("com.baidu.homework", ".activity.user.passport.ChoiceLoginModeActivity")

print(driver.current_package)
print(driver.current_activity)
time.sleep(6)

driver.quit()