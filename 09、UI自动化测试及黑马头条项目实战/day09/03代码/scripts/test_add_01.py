import time


def add(x, y):
    return x+y


class TestAdd:
    # 添加类级别的初始化操作方法
    def setup_class(self):
        print("测试类开始执行时间：",  time.strftime("%Y-%m-%d %H:%M:%S"))

    # 添加类级别的销毁操作方法
    def teardown_class(self):
        print("测试类结束执行时间:", time.strftime("%Y-%m-%d %H:%M:%S"))

    def setup(self):
        print("测试用例开始执行时间:", time.strftime("%Y-%m-%d %H:%M:%S"))

    def test_add_01(self):
        result = add(1, 2)
        assert result == 3

    def test_add_02(self):
        result = add(2, 2)
        assert result == 5

    def teardown(self):
        print("测试用例结束时间:", time.strftime("%Y-%m-%d %H:%M:%S"))