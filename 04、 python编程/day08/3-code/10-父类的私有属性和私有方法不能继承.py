class animal:
    def sleep(self):
        print("睡")

    def __eat(self):  # 私有成员不会被子类继承
        print("吃")

class dog(animal): # 在dog类里面,没有__eat方法
    pass

d = dog()
d.sleep()
# d.__eat()  # 这里的代码会出错