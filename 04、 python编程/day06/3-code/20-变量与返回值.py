a = 1
def my_test1():
    a = 2
    return a  # 函数的返回值都是依赖于return, 一个没有return的函数是没有返回值

def my_test2():
    a = 10

num1 = my_test2()  # 把my_test2的返回值赋值给变量num1

print(my_test1())  # 用print显示my_test1函数的返回值
print(a)

