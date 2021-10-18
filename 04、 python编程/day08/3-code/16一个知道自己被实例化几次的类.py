class dog:
    index = 0   # 定义了一个类属性
    @classmethod
    def count(cls):   # 返回值为类属性index
        return cls.index

    def __init__(self):  # 实例化的时候自动调用init
        dog.index += 1  # 每次实例化的时候类属性index + 1

d1 = dog()
d2 = dog()
d3 = dog()
d4 = dog()
print(dog.count())