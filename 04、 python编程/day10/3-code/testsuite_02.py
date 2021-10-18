import unittest
import testcase_01

suite = unittest.TestSuite()
# suite.addTest(testcase_01.my_test("test_001"))
# suite.addTest(testcase_01.my_test("test_002"))
# 只是把测试用例添加到了测试套件中,并不是执行测试用例
suite.addTest(unittest.makeSuite(testcase_01.my_test))
runner = unittest.TextTestRunner() # 实例化TextTestRunner的对象
runner.run(suite)  # 调用对象的run方法
