class dog:
    name = "小白"
    @classmethod
    def get_name(cls):
        return cls.name

    def demo(self): # 演示如何在普通方法中使用类属性和类方法
        dog.name = "小小白"
        print(dog.get_name())

d = dog()
d.demo()