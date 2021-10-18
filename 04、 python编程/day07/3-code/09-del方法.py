class cat:
    def __init__(self, name = "tom"):
        self.name = name

    def show_name(self):
        print(self.name)

    def __del__(self):
        print("%s销毁了" % self.name)

def my_test1():
    c1 = cat("小猫")
    c1.show_name()

my_test1()   # 程序的第一条执行语句
c = cat()  # c是个对象,同时也是一个变量
c.show_name()  # 这里显示了tom