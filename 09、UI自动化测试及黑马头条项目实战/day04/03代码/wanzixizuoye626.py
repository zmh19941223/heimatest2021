#通过unittest编写自动化测试用例步骤:
# 第一步：导入模块 import unittest
import time
import unittest


# 第二步：实现一个类，这个类必须继承自unittest.TestCase
from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

list = [("13012345678","12345678","8888")]
class my_test01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://tpshop-test.itheima.net/")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    @parameterized.expand(list)
    #定义测试用例01：
    def test_01(self,user,password,code):
        self.driver.find_element(By.CLASS_NAME,("red")).click()
        self.driver.find_element(By.ID,"username").send_keys(user)
        self.driver.find_element(By.ID,"password").send_keys(password)
        self.driver.find_element(By.ID,"verify_code").send_keys(code)
        self.driver.find_element(By.CLASS_NAME,"J-login-submit").click()
    #定义测试用例02，进入地址管理页面：
    def test_02(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[text()='地址管理']").click()
    #定义测试用例03：
    def test_03(self):
        #获取当前地址条数信息：
        num = self.driver.find_element(By.XPATH,"//*[@class='gp_num2']/em[1]").text
        print("当前条数是：", num)
        time.sleep(3)
        #点击新增地址
        self.driver.find_element(By.XPATH,"//*[@class='goodpiece']").click()
        time.sleep(3)
        #切换frame
        self.driver.switch_to.frame(self.driver.find_element(By.ID,"layui-layer-iframe100001"))
        #输入收件人
        self.driver.find_element(By.NAME,"consignee").send_keys("贾金哲")
        #下拉选择框选择城市
        element1 = self.driver.find_element(By.ID,"province")
        element2 = self.driver.find_element(By.ID,"city")
        element3 = self.driver.find_element(By.ID,"district")
        element4 = self.driver.find_element(By.ID,"twon")
        select1 = Select(element1)
        select1.select_by_value("1")
        select2 = Select(element2)
        select2.select_by_value("2")
        select3 = Select(element3)
        select3.select_by_value("3")
        select4 = Select(element4)
        select4.select_by_value("4")
        self.driver.find_element(By.ID,"address").send_keys("天通苑")
        #输入联系电话
        self.driver.find_element(By.CLASS_NAME,"wi40-BFB").send_keys("15565050027")
        #点击保存收货地址
        self.driver.find_element(By.CSS_SELECTOR,".box-ok>span").click()
        #获取新增成功后地址条数信息
        time.sleep(2)
        address2 = self.driver.find_element(By.XPATH,"//*[@class='gp_num2']/em[1]").text
        print("添加地址后地址条数是：", address2)
        #判断新增前后地址条数是否相等，如果不相等则打印"新增地址成功"否则打印"新增地址失败"
        if num != address2:
            print("新增地址打印成功")
        else:
            print("新增地址打印失败")















