name = "张三"

def my_test1():
    global name
    name = "李四"

my_test1()
print(name)