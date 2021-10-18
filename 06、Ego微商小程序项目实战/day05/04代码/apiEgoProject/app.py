# 1 测试Ego项目接口的代码项目地址
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
# 2 Ego项目服务器的根URL
BASE_URL = "http://www.myego.com:13140"
# 3 Token（令牌，维持登录状态）
TOKEN = "bd8f3599604107c0d7eebe1ffe15d84a"
# 4 HEADERS（请求一般都是固定的）
HEADERS = {"Content-Type":"application/json", "token": TOKEN}
# 5 Code（由微信小程序前端生成，用于发送给服务器，来获取token）
CODE = "023tA6DW1eYZoY0g0JzW1bY5DW1tA6DK"