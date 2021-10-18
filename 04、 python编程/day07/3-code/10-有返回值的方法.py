class cat:
    def __init__(self, name = "tom"):
        self.name = name

    # 不想写show_name方法, 只是想把name返回给调用者
    def get_name(self):   # 设计方法管理,得到属性值get_属性名
        return self.name

    def set_name(self, name):  # set_属性名(self, 形参)
        self.name = name

    def show_name(self):  # 在方法中显示属性的值一般show_属性名
        print(self.name)

c = cat()
print(c.get_name())
print(c.show_name()) # 没有return语句的方法或者函数,不要放到print
c1 = cat("小猫")
c1.set_name("加菲猫")
print(c1.get_name())
