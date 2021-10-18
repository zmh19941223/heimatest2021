# 一个函数里面又调用另一个函数
def test1():
    print("我是test1")

def my_func():
    print("我是my_func")

def test2():  # 如果不调用test2函数,那么test1和my_func都不执行
    test1()  # test2内部调用了test1
    my_func()

test2()  # 程序第一条执行的语句

