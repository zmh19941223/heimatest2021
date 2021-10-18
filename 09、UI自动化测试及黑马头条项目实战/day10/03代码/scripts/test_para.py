import pytest


def add(x, y):
    return x+y

@pytest.mark.skip(reason="大于2.0的版本不需要再执行此用例")
class TestAdd:
    @pytest.mark.parametrize("x,y,expect", [(1, 2, 3), (2, 2, 4), (3, 2, 5)])
    def test_add_01(self, x, y, expect):
        result = add(x, y)
        assert expect == result


    # def test_add_02(self):
    #     result = add(2, 2)
    #     assert 4 == result
    #
    # @pytest.mark.run(order=-2)
    # def test_add_03(self):
    #     result = add(3, 2)
    #     assert 5 == result
