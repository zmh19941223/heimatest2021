from appium import webdriver


# 获取驱动对象的方法
class UtilsDriver:
    _driver = None

    # 获取驱动对象的方法
    @classmethod
    def get_app_driver(cls):
        if cls._driver is None:
            des_cap = {
                "platformName": "android",  # 表示的是android  或者ios
                "platformVersion": "5.1.1",  # 表示的是平台系统的版本号
                "deviceName": "****",  # 表示的是设备的ID名称（如果只有一个设备可以用****来代替）
                "appPackage": "com.bjcsxq.chat.carfriend",  # 表示app的包名
                "appActivity": ".module_main.activity.SplashActivity",  # 表示的是app的界面名
                "noReset": True  # 用来记住app的session，如果有登陆或做过初始化的操作，为True时，后面不需要再操作
            }
            cls._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)
        return cls._driver

    # 退出驱动对象的方法
    @classmethod
    def quit_app_driver(cls):
        if cls._driver is not None:
            cls.get_app_driver().quit()
            cls._driver = None
