from selenium import webdriver

class DriverUtil:
    def __init__(self):
        self.driver = None
        self.name = "name"
        print(self._name)

    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.driver.get("http://localhost")
        return self._driver

driver_util = DriverUtil()
driver_util.get_driver()