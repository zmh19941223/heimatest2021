def my_func1():
    a = 1  # a是一个局部变量,只属于my_func1函数
    print(a)

def my_func2():
    a = 2 # a是一个局部变量,只属于my_func2函数
    print(a)

my_func1()  # 调用函数的时候,局部变量a出现了
# my_func1函数调用完毕,a消失了
# 定义函数的时候局部变量并不存在,只有调用函数的时候局部变量出现了
print("end")