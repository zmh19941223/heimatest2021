class animal:
    def sleep(self):
        print("睡")

    def eat(self):
        print("吃")

class dog(animal):
    def sleep(self):
        super().sleep() # 在子类方法中调用父类的sleep方法
        print("睡得更多")

d = dog()
d.sleep() # 扩展了父类的sleep,所以既执行了父类的sleep,又增加了功能