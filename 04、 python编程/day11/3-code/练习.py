# 有一个函数叫digital,返回参数中数字的个数
# 比如参数如果为abc123,返回3
# 参数为hello 返回0
#
# 以参数为”hello 123”和”1a3b”, “你好” 来测试digital函数是否正确

# 思路
# 先从TestCase继承一个子类
# 然后子类中实现一个方法,就是一个测试用例
# 就是一个方法,用参数技术,提供三个元组
# [("hello123", 3),("1a3b", 2), ("你好", 0)]

import unittest
suite = unittest.TestLoader().discover(".", "test*.py")
runner = unittest.TextTestRunner()
runner.run(suite)