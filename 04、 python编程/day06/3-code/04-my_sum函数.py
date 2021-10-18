# def my_sum():
#     a = 5
#     b = 6
#     print(a + b)
# 函数一旦定义完成,就不会再次修改函数内部代码
# my_sum()
def my_sum(a, b):
    print(a + b)
# 函数在定义的时候,有几个参数,调用的时候就要对应几个值
my_sum(5, 6)   # 把5赋值给my_sum函数的a参数,把6赋值给my_sum函数的b参数
num1 = 2
num2 = 3
my_sum(num1, num2)
my_sum(7 + 2, 5 * 3)