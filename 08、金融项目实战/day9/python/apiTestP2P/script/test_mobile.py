import json
import logging
import unittest,requests,app

from api.mobleAPI import mobileAPI
from utils import EncryptUtil,encryted_Request

class testMobile(unittest.TestCase):
    def setUp(self) -> None:
        self.mobile_api = mobileAPI()

    def test01_index(self):
        #1、请求参数
        get_index_url = app.MOBILE_URL + "/phone/index/index"
        req_data = {}
        #2、对参数进行加密
        diyou = EncryptUtil.get_diyou(req_data)
        xmdy = EncryptUtil.get_xmdy(diyou)
        #3、发送请求
        req_param = {"diyou":diyou,"xmdy":xmdy}
        response = requests.post(get_index_url,data=req_param)
        print("encryted response = {}".format(response.json()))
        #4、接收响应数据，并对响应数据进行解密
        diyou_data = response.json().get("diyou")
        decryted_data = EncryptUtil.decrypt_data(diyou_data)
        #5、对解密后的响应数据进行断言
        #将json格式转换为字典
        data = json.loads(decryted_data)
        print("decryted response = {}".format(data))
        self.assertEqual(200,data.get("code"))
        self.assertEqual("success",data.get("result"))

    def test02_login(self):
        #准备参数
        mobile_name = "13012345678"
        pwd = "test123"
        #调用封装的接口发送请求
        data = self.mobile_api.login(mobile_name,pwd)
        print("decryted response = {}".format(data))
        self.assertEqual(200,data.get("code"))
        self.assertEqual("success",data.get("result"))

    def test03_login(self):
        #准备参数
        login_url = app.MOBILE_URL + "/phone/member/login"
        req_data = {"member_name": "13012345678", "password": "test123"}
        #调用封装的发送加密数据的接口
        data = encryted_Request(login_url,req_data)
        #对结果进行断言
        self.assertEqual(200,data.get("code"))
        self.assertEqual("success",data.get("result"))