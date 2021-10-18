num1 = 10
def my_func1():
    global num1  # 函数内部就不存在和全局变量同名的局部变量了
    num1 = 1     # 这里是给全局变量num1修改值

def my_func2():
    print(num1)   # 如果在函数内部不修改全局变量的值,就不用global

print(num1)
my_func1()
print(num1)