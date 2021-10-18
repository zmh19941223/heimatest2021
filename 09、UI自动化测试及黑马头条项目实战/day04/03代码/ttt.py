import time
from parameterized import parameterized
from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

castdata=[("蔡玉虎","#province","北京市","#city","县","#district","密云县","#twon","鼓楼街道","人民广场","18237656460")]

class Test_login(unittest.TestCase):
    @parameterized.expand(castdata)
    def test_01(self,name,province,province_name,city,city_name,district,district_name,town,town_name,detail_name,mobil_phone):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://tpshop-test.itheima.net/")
        driver.find_element_by_css_selector("[class='red'] ").click()
        driver.find_element_by_id("username").send_keys("13012345678")
        driver.find_element_by_name("password").send_keys("12345678")
        driver.find_element_by_css_selector("[class='text_uspa check_cum']>[class='text_cmu']").send_keys("8888")
        driver.find_element_by_xpath("//div[@class='login_bnt']/a[@class='J-login-submit']").click()
        time.sleep(3)
        action=ActionChains(driver)
        action.move_to_element(driver.find_element(By.CSS_SELECTOR,".u-dt"))
        action.perform()
        driver.find_element(By.XPATH,"//*[@class='u-dd']/a[2]").click()
        forward_num=driver.find_element(By.XPATH,"//p[@class='gp_num2']/em[@class='red']").text
        driver.find_element(By.CSS_SELECTOR,"[class='goodpiece'] [class='co_blue']").click()
        time.sleep(5)
        element=driver.find_element(By.ID,"layui-layer-iframe100001")
        driver.switch_to.frame(element)
        driver.find_element(By.CSS_SELECTOR,"[name='consignee']").send_keys(name)
        select=Select(driver.find_element(By.CSS_SELECTOR,province))
        select.select_by_visible_text(province_name)
        time.sleep(2)
        select = Select(driver.find_element(By.CSS_SELECTOR, city))
        select.select_by_visible_text(city_name)
        time.sleep(2)
        select = Select(driver.find_element(By.CSS_SELECTOR, district))
        select.select_by_visible_text(district_name)
        time.sleep(2)
        select = Select(driver.find_element(By.CSS_SELECTOR, town))
        select.select_by_visible_text(town_name)
        time.sleep(2)
        driver.find_element(By.ID,"address").send_keys(detail_name)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"[name='mobile']").send_keys(mobil_phone)
        driver.find_element(By.CSS_SELECTOR,"[class='box-ok ma-le--70']").click()
        driver.switch_to.default_content()
        current_num = driver.find_element(By.XPATH, "//p[@class='gp_num2']/em[@class='red']").text
        if forward_num!=current_num:
            print("新增地址成功")
        else:
            print("新增地址失败")

        driver.quit()