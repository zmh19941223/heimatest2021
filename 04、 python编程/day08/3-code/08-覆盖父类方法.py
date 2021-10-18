class animal:
    def sleep(self):
        print("睡")

    def eat(self):
        print("吃")

class dog(animal):
    def eat(self):  # 出现和父类同名方法,在子类dog中,就没有父类的eat方法了
        print("吃肉")

d = dog()
d.sleep()
d.eat()  # 由于覆盖了父类的eat方法,,所以这里调用的是dog类的eat方法