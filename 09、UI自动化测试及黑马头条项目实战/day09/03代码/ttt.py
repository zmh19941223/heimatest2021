class Testlogin:
    def test_01(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://tpshop-test.itheima.net/Home/Index/index.html")
        driver.find_element(By.ID, 'red').click()
        driver.find_element(By.CSS_SELECTOR, "#username").send_keys()
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("12345678")
        driver.find_element(By.CSS_SELECTOR, "#verify_code").send_keys("8888")
        driver.find_element(By.ID, "J-login-submit").click()

    def test_02(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://tpshop-test.itheima.net/Home/Index/index.html")
        driver.find_element(By.CSS_SELECTOR, '.red').click()
        driver.find_element(By.CSS_SELECTOR, "#username").send_keys("13012345678")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys()
        driver.find_element(By.CSS_SELECTOR, "#verify_code").send_keys("8888")
        driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()