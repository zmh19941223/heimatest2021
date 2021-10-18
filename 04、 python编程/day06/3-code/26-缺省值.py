def my_test1(a, b = 10):  # 形参b有缺省值
    print(a, b)

def my_test2(a = 1, b = 2):
    print(a, b)

my_test1(1, 2)
my_test1(100)
my_test2()
my_test2(100, 12)

# def my_test3(a = 10, b):  不能把有缺省值的形参写到没缺省值形参的前面
#     print(a, b)

