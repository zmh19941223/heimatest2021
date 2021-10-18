import pytest


def add(x, y):
    return x+y


class TestADD:  # 定义的类名必须是以Test开头
    def test_add_01(self):  # 定义的测试方法必须是以test开头
        result = add(1, 2)
        print(result)
        # assert result == 3    判断相等
        # assert result != 4    判断不相等
        # assert result    # 判断为True
        #assert False        # 判断为False
        # assert "a" in "abc" # 判断包含
        # assert "a" not in "abc"  # 判断不包含
        # assert result is None
        assert result is not None

    def test_add_02(self):
        result = add(2, 2)
        print(result)

