import time


def add(x, y):
    return x+y


class TestAdd:

    def setup(self):
        print("测试用例开始执行时间:", time.strftime("%Y-%m-%D %H:%M:%S"))

    def test_add_01(self):
        result = add(1, 2)
        assert result == 3

    def test_add_02(self):
        result = add(2, 2)
        assert result == 4

    def teardown(self):
        print("测试用例结束时间:", time.strftime("%Y-%m-%D %H:%M:%S"))