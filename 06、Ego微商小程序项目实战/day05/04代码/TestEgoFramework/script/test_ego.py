# 导包
import unittest
import logging
import app
from api.ego_api import EgoApi

class TestEgo(unittest.TestCase):

    def setUp(self):
        # 手动设置token
        app.HEADERS["token"] = "7d9aad58b807468296e342fa8c06ec73"

    @classmethod
    def setUpClass(cls):
        cls.ego_api = EgoApi() # 实例化封装EgoApi类

    def test01_get_banner_success(self):
        # 使用实例化的ego_api发送获取轮播图的接口请求
        response = self.ego_api.get_banner()
        # 打印响应数据
        logging.info("正向用例获取轮播图的测试结果为：{}".format(response.json()))
        # 断言结果
        self.assertEqual(200, response.status_code) # 断言响应状态码是不是200
        self.assertEqual("首页轮播图", response.json().get("description")) #断言返回响应数据中description

    def test02_get_theme_success(self):
        # 先使用实例化的ego_api来获取专题栏位
        response = self.ego_api.get_theme("ids=1,2,3")
        # 打印响应数据
        logging.info("测试获取的专题栏位为：{}".format(response.json()))
        # 断言结果
        self.assertEqual(200, response.status_code) # 断言响应状态码是不是200
        logging.info('response.json()[0].get("description")的结果为：{}'.format(response.json()[0].get("description")))
        self.assertEqual("美味水果世界", response.json()[0].get("description")) #断言返回响应数据中description

    def test03_get_recent_goods(self):
        # 发送获取最近新品的接口请求
        response = self.ego_api.get_recent_goods()
        # 打印日志
        logging.info("测试获取最近新品接口：{}".format(response.json()))
        # 断言结果
        self.assertEqual(200, response.status_code)
        logging.info('response.json()[0].get("name"):{}'.format(response.json()[0].get("name")))
        self.assertEqual("芹菜 半斤", response.json()[0].get("name"))

    def test04_get_goods_category(self):
        # 发送获取商品分类的接口请求
        response = self.ego_api.get_product_category()
        # 打印日志
        logging.info("获取商品分类为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("果味", response.json()[0].get("name"))

    def test05_get_category_any_goods(self):
        # 发送获取商品分类下的商品接口请求
        response = self.ego_api.by_category("2")
        # 打印结果
        logging.info("获取商品分类下的商品接口请求结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("梨花带雨 3个", response.json()[0].get("name"))

    def test06_get_goods_detail(self):
        # 发送获取商品详情的接口请求
        response = self.ego_api.get_product_detail("32")
        # 打印结果
        logging.info("获取商品详情接口的结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("土豆 半斤", response.json().get("name"))

    def test07_get_token(self):
        # 发送获取token的接口请求
        response = self.ego_api.get_token(app.HEADERS,
                                          {"code":"003bik0n04KpCn1Saz1n0hlzKQ3bik00"})
        # 打印结果
        logging.info("获取的token为：{}".format(response.json()))

        # 断言
        self.assertEqual(200, response.status_code)
        logging.info("response.json().get('token'): {}".format(response.json().get("token")))
        self.assertTrue(response.json().get("token")) # 断言获取的token是否存在

    def test08_verify_token(self):
        # 发送验证token的接口请求
        response = self.ego_api.verify_token({"token":"7d9aad58b807468296e342fa8c06ec73"})
        # 打印验证的结果
        logging.info("验证的结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code) # 断言响应状态码
        self.assertTrue(response.json().get("isValid")) #断言响应数据中有没有isValid

    def test09_get_user_orderlist(self):
        # 发送获取用户订单列表的接口请求
        response = self.ego_api.get_user_orderlist(app.HEADERS, "page=1") # 注意：我们在setup中已经提前手动设置了token，所以能够在这里直接引用app.HEADERS
        # 打印获取的结果
        logging.info("获取用户订单列表的结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertIn("夏日芒果", response.json().get('data')[0].get("snap_name"))

