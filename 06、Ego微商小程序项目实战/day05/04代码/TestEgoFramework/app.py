# 定义全局变量
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 项目根目录
BASE_URL = "http://www.myego.com:13140" #ego微商服务器域名
TOEKN = "71ce3a105b89b2bc82fb3bd21ecc1a99" # 注意令牌可能会失效，也是使用code之后，获取的令牌，也需要手动设置
HEADERS = {"Content-Type": "application/json"}
CODE = "093yS0000rF93K1KH9000WxFJ21yS00Q" # code是手动从微信小程序前端获取的