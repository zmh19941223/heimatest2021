class dog:
    name = "二哈"   # 如果在这个位置定义的变量,就是类属性
    @classmethod
    def set_name(cls, name):
        cls.name = name   # 通过类方法的形参修改类属性name值

    def __init__(self):
        self.age = 20  # 在类方法里面无法访问age

    def demo(self):  # 在类方法中无法调用demo
        print("普通方法")

print(dog.name)  # 显示类属性的值
dog.name = "狼狗"  # 修改类属性的值
print(dog.name)
dog.set_name("比熊")
print(dog.name)