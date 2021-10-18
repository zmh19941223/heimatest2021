class dog:
    name = "小白"
    @classmethod
    def get_name(cls):
        return cls.name

    def __init__(self):
        self.age = 0
    def get_age(self):
        return self.age
# 要把类属性name的值修改为"小小白"
dog.name = "小小白"
# 调用类方法get_name,显示name的值
print(dog.get_name())
# 要把普通属性age的值修改为10
d = dog()
d.age = 10
# 调用普通方法get_age显示age的值
print(d.get_age())