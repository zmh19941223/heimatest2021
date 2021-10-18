class cat:  # 定义了一个类cat,这个类不能直接使用
    def set_name(self):
        self.name = "tom"  # 定义了一个属性,名叫name,值是tom

    def eat(self):  # 第一个参数必须是self
        print("%s吃饭" % self.name) # 这里在使用name属性
    def drink(self):
        print("%s喝水" % self.name) # 这里在使用name属性

    def demo(self):  # 这个方法只是为了举例,在类的内部,方法嵌套调用
        self.eat()
        self.drink()

c = cat()
c.set_name()
c.drink()
c.eat()
c.name = "张三"
c.drink()
c.eat()
c.demo()