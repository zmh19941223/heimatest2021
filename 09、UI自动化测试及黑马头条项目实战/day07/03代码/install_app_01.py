# 导入webdriver
import time

from appium import webdriver
# 初始化app的配置信息
des_cap = dict()  # 定义字典参数

des_cap["platformName"] = "android"   # 表示的是android 或者IOS系统
des_cap["platformVersion"] = "5.1.1"  # 表示的是平台系统的版本号
des_cap["deviceName"] = "****"  # 表示的是设备的ID名称（如果只有一个设备可以用****来替代）
des_cap["appPackage"] = "com.android.settings"  # 表示的是app的包名
des_cap["appActivity"] = ".Settings"  # 表示的是app的界面名

driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)
# driver.close_app()
time.sleep(2)
# 判断手机是否安装了对应的app

driver.background_app(5)
print(driver.is_app_installed("com.android.settings"))

print(driver.is_app_installed("com.em.mobile"))
# 安装263app
# driver.install_app(r"D:\BaiduNetdiskDownload\apptools\apk\263.apk")

# 卸载263app
# driver.remove_app("com.em.mobile")
time.sleep(3)
driver.quit()
