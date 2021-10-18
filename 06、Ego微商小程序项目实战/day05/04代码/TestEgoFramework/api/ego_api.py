# 使用requests
import requests

import app


class EgoApi:

    def __init__(self):
        self.banner_url = app.BASE_URL + "/api/v1/banner/1"
        self.theme_url = app.BASE_URL + "/api/v1/theme"
        self.recent_goods_url = app.BASE_URL + "/api/v1/product/recent"
        self.token_url = app.BASE_URL + "/api/v1/token/user"
        self.address_url = app.BASE_URL + "/api/v1/address"
        self.verify_token_url = app.BASE_URL + "/api/v1/token/verify"
        self.orderlist_url = app.BASE_URL + "/api/v1/order/by_user"
        self.create_order_url = app.BASE_URL + "/api/v1/order"
        self.query_order_url = app.BASE_URL + "/api/v1/order"
        self.category_url = app.BASE_URL + "/api/v1/category/all"
        self.by_category_url = app.BASE_URL + "/api/v1/product/by_category"
        self.product_detail_url = app.BASE_URL + "/api/v1/product"

    # 获取轮播图
    def get_banner(self):
        return requests.get(url=self.banner_url)

    # 获取专题栏位
    def get_theme(self, ids):
        return requests.get(url=self.theme_url, params=ids)

    # 获取最近新品
    def get_recent_goods(self):
        return requests.get(url=self.recent_goods_url)

    # 获取令牌
    def get_token(self, headers, json):
        return requests.post(url=self.token_url, headers=headers, json=json)

    # 获取地址
    def get_address(self, headers):
        return requests.get(url=self.address_url, headers=headers)

    # 验证令牌是否有效
    def verify_token(self, json):
        return requests.post(url=self.verify_token_url,json=json)

    # 封装获取用户订单列表
    def get_user_orderlist(self, headers,page): # "page=1"
        return requests.get(url=self.orderlist_url, params=page,headers=headers)

    # 封装创建订单接口
    def create_order(self, headers, json):
        return requests.post(url=self.create_order_url,
                             headers=headers,
                             json=json)

    # 封装查看订单接口
    def query_order(self, headers, order_id):
        """
        :param headers:
        :param order_id: 是order表中的id属性，而不是order_no
        :return:
        """
        query_order_url = self.query_order_url + "/" + order_id
        print("拼接的查看订单接口的URL", query_order_url)
        return requests.get(url=query_order_url, headers=headers)

   # 获取商品分类
    def get_product_category(self):
        return requests.get(self.category_url)

    # 获取商品分类下的某个商品
    def by_category(self, params):
        return requests.get(self.by_category_url, params={"id":params})

    # 获取商品信息
    def get_product_detail(self, product_id):
        url = self.product_detail_url + "/" + product_id # 拼接获取商品信息的URL
        return requests.get(url=url)

if __name__ == '__main__':
    ego_api = EgoApi() # 实例化egoapi类
    response = ego_api.get_banner() # 发送获取轮播图的接口请求
    print(response.json()) # 打印轮播图的结果

    response = ego_api.get_theme("ids=1,2,3")
    print(response.json()) # 打印专题栏位的结果

    response = ego_api.get_recent_goods() # 获取最近新品
    print("最近新品：", response.json())

    response = ego_api.get_token(app.HEADERS, {"code":app.CODE})
    print("获取的令牌为：",response.json())

    print("更新前的app.HEADERS:", app.HEADERS)
    app.HEADERS["token"] = "71ce3a105b89b2bc82fb3bd21ecc1a99" # 设置token
    print("更新之后的app.HEADERS为：",app.HEADERS)
    response = ego_api.get_address(app.HEADERS)
    print("使用令牌后，获取地址的信息为：", response.json())

    response = ego_api.verify_token({"token":"71ce3a105b89b2bc82fb3bd21ecc1a99"})
    print("验证令牌的结果为", response.json())

    app.HEADERS["token"] = "1bf579b4b83f092e0a5be229a510219a"  # 设置token
    response = ego_api.get_user_orderlist(app.HEADERS,"page=2")
    print("获取的用户订单列表为：", response.json())

    app.HEADERS["token"] = "1bf579b4b83f092e0a5be229a510219a"  # 设置token
    response = ego_api.create_order(app.HEADERS, {"products":[{"product_id":8,"count":1},{"product_id":10,"count":2}]})
    print("创建订单的结果为：", response.json())

    app.HEADERS["token"] = "1bf579b4b83f092e0a5be229a510219a"  # 设置token
    response = ego_api.query_order(app.HEADERS, "110")
    print("查询订单的结果为：", response.json())