# 试一下不封装时，访问ego微商项目的获取轮播图的接口

# 导入requests
import requests
# 使用requests模块按照接口文档的要求发送接口请求
response = requests.get(url="http://www.myego.com:13140/api/v1/banner/1")
# 打印响应数据
print(response.json())

# 使用requests模块按照专题栏位的要求发送接口请求
response = requests.get(url="http://www.myego.com:13140/api/v1/theme?ids=1")
# 打印响应结果
print(response.json())

# 使用requests模块按照最近新品的要求发送接口请求
response = requests.get(url="http://www.myego.com:13140/api/v1/product/recent")
# 打印响应结果
print(response.json())

# 使用requests模块来获取令牌
# 在令牌中，需要使用ego前端手动获取的code来得到令牌
response = requests.post(url="http://www.myego.com:13140/api/v1/token/user",
                         headers={"Content-Type":"application/json"},
                         json={"code":"003vhd0n0oZuCn1EOV2n0hubIs0vhd0q"})

# 打印结果
print("获取令牌结果为：", response.json())

# 使用requests模块快发送获取地址信息的接口请求
response = requests.get(url="http://www.myego.com:13140/api/v1/address",
                         headers={"token":"de05aee5ad7d9d21c9b6e043a340673f"})
# 打印结果
print(response.json())

# 使用requests模块发送Token验证接口，验证获取到的token是不是有效的token
response = requests.post(url="http://www.myego.com:13140/api/v1/token/verify",
                         headers={"Content-Type":"application/json"},
                         json={"token":"1bf579b4b83f092e0a5be229a510219a"})
# 打印结果
print("验证token的结果：", response.json())