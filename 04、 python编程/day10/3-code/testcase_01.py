import unittest

def my_sum(a, b):
    return a + b

class my_test(unittest.TestCase):
    def test_001(self):
        print(my_sum(5, 6))

    def test_002(self):
        print(my_sum(0, 3))


