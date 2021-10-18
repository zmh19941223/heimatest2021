name = "张三"
def my_test1():
    global name
    name = "李四"  # 这里修改的是全局变量的值

my_test1()
# 从这里开始全局变量name的值已经成了"李四"了


print(name)