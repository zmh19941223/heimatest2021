num1 = 1
def my_func1():
    num1 = 10   # 这里不是为全局变量赋值, 这里是定义了一个局部变量, 名字和全局变量重名
    print(num1) # 打印的是局部变量num1的值
    num1 += 1   # 这里改的是局部变量num1的值

def my_func2():
    print(num1) # 全局变量num1

my_func1()
my_func2()
print(num1) # 打印的是全局变量num1的值