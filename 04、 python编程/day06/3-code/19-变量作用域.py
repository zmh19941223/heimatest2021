a = 1

def my_test1():
    global a
    a = 2

def my_test2():
    a = 3   # 这里的a是一个只在my_test2里面的局部变量
    my_test1()

print(a)  # 程序入口在这里
my_test2()
print(a)

