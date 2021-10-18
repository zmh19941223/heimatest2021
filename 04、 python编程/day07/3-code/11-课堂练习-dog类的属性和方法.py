# 有一个dog类,有属性name和age
# 提供设置,得到,显示name和age属性的方法
class dog:
    def __init__(self, name = '二哈', age = 2):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def show_name(self):
        print(self.name)

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def show_age(self):
        print(self.age)

d = dog("比熊", 3)  # 实例化的时候设置属性的值
print(d.get_name())
d.set_name("黑背") # 实例化以后再设置属性值
print(d.get_name())
d.show_name()