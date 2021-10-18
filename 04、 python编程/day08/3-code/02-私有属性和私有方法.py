class woman:
    def __init__(self):
        self.name = "玛丽"
        self.__weight = 200  # __weigth是一个私有属性

    def __eat(self):   # __eat方法为私有方法
        print("吃的很多")



w = woman()
print(w.name)
# print(w.__weight)  不能在类的外部访问类的私有属性
# w.__eat()   不能在类的外部调用私有方法