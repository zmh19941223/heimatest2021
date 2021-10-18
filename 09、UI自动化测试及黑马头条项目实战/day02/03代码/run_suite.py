import unittest
# 定义测试套件
from HTMLTestRunner import HTMLTestRunner

from scripts.login_test import TestLogin

suite = unittest.TestSuite()
# 往套件添加测试用例
suite.addTest(unittest.makeSuite(TestLogin))
filename = 'test.html'
with open(filename, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="自动化测试报告", description="web-chrome-1.0")
    runner.run(suite)

# # 定义测试运行器
# runner = unittest.TextTestRunner()
#
# # 通过runner运行测试套件
# runner.run(suite)