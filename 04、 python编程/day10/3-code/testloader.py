import unittest
from HTMLTestRunner import HTMLTestRunner
# 用TestLoader对象的discover方法来自动查找py,自动加载py文件中的方法
# 第一个参数是从哪里找py文件,"."从当前目录开始查找py文件
# 第二个参数是指定py文件的文件名,可以用通配符
suite = unittest.TestLoader().discover(".", "my*.py")
# runner = unittest.TextTestRunner()
file = open("test01.html", "wb")  # 用wb代表用二进制写方式打开文件
# runner = unittest.TextTestRunner(stream=file, verbosity=2)
runner = HTMLTestRunner(stream=file, title="我的第一个html测试报告")
runner.run(suite)
file.close()