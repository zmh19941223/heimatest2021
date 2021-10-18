# 1,导入模块unittest
import unittest

import time

from selenium.webdriver.support.select import Select


class Test(unittest.TestCase):
# 2,进入tpshop首页并登陆
    from selenium import webdriver
    driver =webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://tpshop-test.itheima.net/')

    driver.find_element_by_class_name('red').click()
    driver.find_element_by_id('username').send_keys('13012345678')
    driver.find_element_by_id('password').send_keys('12345678')
    driver.find_element_by_id('verify_code').send_keys('8888')
    driver.find_element_by_name('sbtbutton').click()
# 3.进入地址管理界面
    time.sleep(3)
    driver.find_element_by_xpath('//*[text()="地址管理"]').click()
# 4.获取当前地址条数信息
    time.sleep(3)
    sum1=driver.find_element_by_xpath('//em[@class="red"]')
    print(sum1.text)
# 5.新增一条地址
    driver.find_element_by_class_name('co_blue').click()
    time.sleep(5)
    driver.find_element_by_name('consignee').send_keys('小肖')
    elment1 = driver.find_element_by_css_selector('[name="province"]')
    select=Select(elment1)
    select.select_by_value('25579')

    elment2=driver.find_element_by_css_selector('[name="city"]')
    select=Select(elment2)
    select.select_by_value('26001')
    elment3=driver.find_element_by_id('district')
    select=Select(elment3)
    select.select_by_value('26112')

    driver.find_element_by_css_selector('[class="he110 wi80-BFB re-no"]').send_keys('衡山县xx街道')
    driver.find_element_by_name('mobile').send_keys('13522227890')
    driver.find_element_by_xpath('//*[text()="保存收货地址"]').click()
    time.sleep(3)
# 6.获取新增成功后地址条数信息，判断新增前后地址条数是否相等如不相等则打印"新增地址成功"否则打  印"新增地址失败"
    sum2=driver.find_element_by_xpath('//em[@class="red"]')
    if sum2.text==sum1.text:
        print('新增地址失败')
    else:
        print('新增地址成功')
    time.sleep(2)
    driver.quit()
