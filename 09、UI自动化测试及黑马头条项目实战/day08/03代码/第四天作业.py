import unittest
# 1.要求使用unittest组织测试用例
# 2.进入tpshop首页并登陆
# 3.进入地址管理界面
# 4.获取当前地址条数信息
# 5.新增一条地址
# 6.获取新增成功后地址条数信息，判断新增前后地址条数是否相等如不相等则打印"新增地址成功"否则打
# 印"新增地址失败"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestAddAddress(unittest.TestCase):
    def test_add_address_01(self):

        driver = webdriver.Chrome()  # 创建浏览器驱动对象
        driver.maximize_window()
        driver.implicitly_wait(10)

        # 打开topshop首页
        driver.get("http://tpshop-test.itheima.net/")
        # 点击登陆跳转到登录页面
        driver.find_element(By.CSS_SELECTOR, ".red").click()
        # 输入用户名、密码、验证码
        driver.find_element(By.ID, "username").send_keys("13012345678")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.ID, "verify_code").send_keys("8888")

        # 点击登录按钮
        driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()

        # 点击地址管理跳转到地址管理页面
        driver.find_element(By.XPATH, "//*[@class='menu-ul']/ul[4]/li[4]/a").click()

        # 打印地址的条数
        numbers = driver.find_element(By.XPATH, "//*[@class='gp_num2']/em[1]").text
        print("当前地址条数为：", driver.find_element(By.XPATH, "//*[@class='gp_num2']/em[1]").text)

        # 新增地址
        # 点击增加新地址
        driver.find_element(By.XPATH, "//*[text()='增加新地址']").click()
        # 切换到iframe窗口
        address_frame = driver.find_element(By.ID, "layui-layer-iframe100001")
        driver.switch_to.frame(address_frame)

        # 输入收货人信息
        driver.find_element(By.NAME, "consignee").send_keys("testt")
        # 选择地址  选择省 市  区 镇
        select_province = Select(driver.find_element(By.ID, "province"))
        select_province.select_by_value("1")

        select_city = Select(driver.find_element(By.ID, "city"))
        select_city.select_by_value("2")

        select_district = Select(driver.find_element(By.ID, "district"))
        select_district.select_by_index(3)
        # 输入详细地址
        driver.find_element(By.ID, "address").send_keys("testsetestest")
        # 输入电话号码
        driver.find_element(By.NAME, "mobile").send_keys("13099998888")

        # 点击保存收货地址
        driver.find_element(By.XPATH, "//*[text()='保存收货地址']").click()

        # 获取的是增加新地址之后的数量
        after_numbers = driver.find_element(By.XPATH, "//*[@class='gp_num2']/em[1]").text

        # 判断新增前的地址信息是否相等
        if int(numbers) == int(after_numbers):
            print("新增地址失败!")
        else:
            print("新增地址成功!")
