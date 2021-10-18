import pytest


def add(x, y):
    return x+y

version = 21
# @pytest.mark.skipif(version > 20, reason="大于2.0的版本不需要再执行此用例")
class TestAdd:
    @pytest.mark.last    # 设置用例最后执行
    def test_add_01(self):
        result = add(1, 2)
        assert 3 == result


    # @pytest.mark.skip("版本已更新，不需要再进行测试")
    @pytest.mark.run(order=0)
    def test_add_02(self):
        result = add(2, 2)
        assert 4 == result

    @pytest.mark.run(order=-2)
    def test_add_03(self):
        result = add(3, 2)
        assert 5 == result
