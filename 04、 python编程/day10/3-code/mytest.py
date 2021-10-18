import unittest
from parameterized import parameterized

def my_sum(a, b):
    return a + b

def get_data():  # 定义了一个函数,返回一个列表
    return [(1, 2, 3), (5, 6, 101), (-1, 3, 2)]

class my_test1(unittest.TestCase):
    # a是调用my_sum的第一个参数
    # b是调用my_sum的第二个参数
    # c是预期结果
    @parameterized.expand(get_data())
    def test_001(self, a, b, c):
        num1 = my_sum(a, b)  # 定义变量num1得到my_sum函数的返回值
        self.assertEqual(num1, c)  # num1里存放的是实际结果,11是预期结果
        # 实际结果与预期结果相符,代表测试用例测试通过
        # 不相符代表测试用例测试失败
    @unittest.skip
    def test_002(self):
        print("test002")




