import json

import requests

import app
from utils import EncryptUtil


class mobileAPI():
    def __init__(self):
        self.login_url = app.MOBILE_URL + "/phone/member/login"
        self.get_user_info = app.MOBILE_URL + "/phone/member/userInfo"

    def login(self,member_name,pwd):
        #准备测试数据
        req_data = {"member_name": member_name,"password": pwd}
        #对数据进行加密
        diyou = EncryptUtil.get_diyou(req_data)
        xmdy = EncryptUtil.get_xmdy(diyou)
        #发送请求
        req_param =  {"diyou":diyou,"xmdy":xmdy}
        response = requests.post(self.login_url,data=req_param)
        #接收响应并解密
        diyou_data = response.json().get("diyou")
        data = EncryptUtil.decrypt_data(diyou_data)
        result = json.loads(data)
        #返回解密后结果
        return result


