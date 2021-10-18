# 导入requests模块
import requests
import app
# 创建API接口类
class EgoApi:

    def __init__(self):
        # 定义轮播图的url
        self.banner_url = app.BASE_URL + "/api/v1/banner/1"
        # 定义专题栏位的url
        self.theme_url = app.BASE_URL + "/api/v1/theme"
        # 最近新品的URL
        self.recent_product_url = app.BASE_URL + "/api/v1/product/recent"
        # 获取商品分类url
        self.category_url = app.BASE_URL + "/api/v1/category/all"
        # 获取商品分类下的某个商品
        self.by_category_url = app.BASE_URL + "/api/v1/product/by_category"
        # 获取商品详情
        self.product_detail_url = app.BASE_URL + "/api/v1/product"
        # 获取用户订单列表
        self.order_list_url = app.BASE_URL + "/api/v1/order/by_user"
        # 创建订单URL
        self.create_order_url = app.BASE_URL + "/api/v1/order"
        # 查看订单详情
        self.order_detail_url = app.BASE_URL + "/api/v1/order"
        # 获取Token
        self.get_token_url = app.BASE_URL + "/api/v1/token/user"
        # 验证token的url
        self.verify_token_url = app.BASE_URL + "/api/v1/token/verify"
        # 获取地址信息的URL
        self.get_address_url = app.BASE_URL + "/api/v1/address"
    # 轮播图
    def get_banner(self):
        return requests.get(self.banner_url)

    # 专题栏位
    def theme(self, params):
        return requests.get(self.theme_url, params={"ids":params})

    # 最近新品
    def recent_product(self):
        return requests.get(self.recent_product_url)

    # 获取商品分类
    def get_product_category(self):
        return requests.get(self.category_url)

    # 获取商品分类下的某个商品
    def by_category(self, params):
        return requests.get(self.by_category_url, params={"id":params})

    # 获取商品信息
    def get_product_detail(self, product_id):
        return requests.get(self.product_detail_url + "/" + str(product_id))

    # 获取用户订单列表（登录后的接口）
    def get_order_list(self, page):
        return requests.get(self.order_list_url, params={"page":page}, headers=app.HEADERS)

    # 创建订单
    def create_order(self, jsondata):
        return requests.post(self.create_order_url, json=jsondata, headers=app.HEADERS)

    # 查看订单
    def get_order_detail(self, order_id):
        return requests.get(self.order_detail_url + "/" + str(order_id), headers=app.HEADERS)

    # 获取Token
    def get_token(self, code):
        return requests.post(self.get_token_url, json={"code": code})

    # Token验证接口
    def verify_token(self, token):
        return requests.post(self.verify_token_url, json={"token": token})

    # 获取地址信息
    def get_address(self):
        return requests.get(self.get_address_url, headers=app.HEADERS)

