# 导包
import unittest
import app
from script.test_ego import TestEgo
from lib.HTMLTestRunner import HTMLTestRunner
# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例的代码添加到测试套件中
suite.addTest(unittest.makeSuite(TestEgo))
# 定义测试报告的路径和名称
report_name = app.BASE_DIR + "/report/mini.html"
# 使用HTMLTestRunner运行测试套件生成测试报告
with open(report_name, 'wb') as f:
    # 初始化HTMLTestRunner
    runner = HTMLTestRunner(f, verbosity=1, title="Ego微商", description="测试Ego微商的常见接口")
    # 使用实例化的runner运行测试套件，并生成测试报告
    runner.run(suite)