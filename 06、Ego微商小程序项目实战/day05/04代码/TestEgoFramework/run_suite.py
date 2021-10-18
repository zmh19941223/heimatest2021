
# 导包
import unittest
# 创建测试套件
import app
from lib import HTMLTestRunner
from script.test_ego import TestEgo

suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestEgo))
# 定义测试报告的名称
reportname = app.BASE_DIR + "/report/mini_ego.html"
# 使用HTMLTestRunner生成测试报告
with open(reportname, mode="wb") as f:
    # 实例化HTMLTestRunner
    runner = HTMLTestRunner.HTMLTestRunner(f, verbosity=2, title="Ego商城的接口测试报告")
    # 使用runner运行测试套件
    runner.run(suite)