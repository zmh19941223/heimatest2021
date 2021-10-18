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

driver = webdriver.Remote("http://192.168.1.100:4723/wd/hub", des_cap)
# 关闭当前的app（是可以再重新启动新的app）
driver.close_app()
time.sleep(2)
driver.start_activity("com.baidu.homework", ".activity.user.passport.ChoiceLoginModeActivity")
time.sleep(6)
# 退出驱动  切换了代码与appium服务器这间的连接，所以不能再往后操作（启动app）
driver.quit()
