import unittest
from parameterized import parameterized
def digital(str1):
    sum = 0
    for n in str1:
        if n >= "0" and n <= "9":
            sum += 1
    return sum

class MyTest(unittest.TestCase):
    @parameterized.expand([("hello123", 3),("1a3b", 2), ("你好", 0)])
    def test_001(self, a, b):
        num1 = digital(a)
        self.assertEqual(num1, b)

