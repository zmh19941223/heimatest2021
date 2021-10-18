class father:
    def __init__(self):
        self.__name = "张三"
        self.house = "别墅"
    def eat(self):
        print("吃")
    def sleep(self):
        print("睡")
    def __edu_back(self):
        print("本科")

class son(father):  # son拥有father所有的方法和属性
    def show_eat(self):
        self.eat()    # eat是继承自father的,但也是son自己的

    def show_sleep(self):
        self.sleep()

    def show_house(self):
        print(self.house) # house是一个属性,不能调用,要用print

s = son()
s.show_eat()
s.show_sleep()
s.show_house()

# father有两个属性,三个方法
# son继承了father一个属性,两个方法
