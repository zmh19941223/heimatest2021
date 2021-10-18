# 导包
import unittest
import logging

import app
from api.ego_api import EgoApi

# 创建测试类
class TestEgo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 实例化EgoApi类
        cls.ego_api = EgoApi()

    # 测试获取轮播图
    def test01_get_banner(self):
        # 使用封装的接口获取轮播图
        response = self.ego_api.get_banner()
        # 打印结果
        logging.info("获取轮播图的结果为：{}".format(response.json()))

        # 断言结果
        self.assertEqual(200, response.status_code) # 断言响应状态码
        self.assertEqual(['6', '25', '11', '21', '10'], [i.get("key_word") for i in response.json().get('items')])

    # 测试获取专题栏位
    def test02_get_theme(self):
        # 使用封装的接口获取专题栏位
        response = self.ego_api.theme("1,2,3")
        # 打印结果
        logging.info("获取专题栏位为：{}".format(response.json()))

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("美味水果世界", response.json()[0].get("description"))

    # 测试获取最近新品
    def test03_get_recent_data(self):
        # 使用封装的接口获取最近新品
        response = self.ego_api.recent_product()
        # 打印结果
        logging.info("获取最近新品为：{}".format(response.json()))

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("芹菜 半斤", response.json()[0].get('name'))

    # 获取商品分类
    def test04_get_category(self):
        # 使用封装的接口获取商品分类
        response = self.ego_api.get_product_category()
        # 打印结果
        logging.info("获取商品分类为：{}".format(response.json()))

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("果味", response.json()[0].get("name"))

    # 获取商品分类下的商品
    def test05_get_product(self):
        # 使用封装的接口获取商品分类下的商品
        response = self.ego_api.by_category(2)
        # 打印结果
        logging.info("获取商品分类下的商品为：{}".format(response.json()))

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("梨花带雨 3个", response.json()[0].get("name"))

    # 获取商品详情
    def test06_get_product_detail(self):
        # 使用封装的接口获取商品详情
        response = self.ego_api.get_product_detail(2)
        # 打印结果
        logging.info("获取商品商品详情：{}".format(response.json()))

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("梨花带雨 3个", response.json().get("name"))

    # 获取Token
    def test07_get_token(self):
        # 使用封装的接口获取token
        response = self.ego_api.get_token(app.CODE)
        # 打印结果
        logging.info("获取token：{}".format(response.json()))

        # 断言
        self.assertEqual(200, response.status_code)

    # 验证token是否正确
    def test08_verify_token(self):
        # 发送获取token的接口请求
        response = self.ego_api.verify_token(app.TOKEN)
        # 打印结果
        logging.info("获取token的接口请求：{}".format(response.json()))

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("isValid"))

    # 验证获取用户订单列表
    def test09_get_order_list(self):
        # 发送获取用户订单列表的请求
        response = self.ego_api.get_order_list(1,)
        # 打印结果
        logging.info("获取用户订单列表的请求：{}".format(response.json()))

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("夏日芒果 3个", response.json().get("data")[0].get("snap_name"))

    # 创建订单
    def test10_create_order(self):
        # 创建订单
        response = self.ego_api.create_order({"products":[{"product_id":8,"count":1}]})
        # 打印结果
        logging.info("创建订单：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("pass"))

    # 查看订单
    def test11_get_order_detail(self):
        # 查看订单
        response = self.ego_api.get_order_detail(50)
        # 打印结果
        logging.info("查看订单：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(3, response.json().get("total_count"))

    # 获取用户地址信息
    def test12_get_address(self):
        # 获取用户地址
        response = self.ego_api.get_address()
        # 打印
        logging.info("获取用户地址：{}".format(response.json()))

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("17620332300", response.json().get("mobile"))

