# # 我们没有使用过函数 带返回值
# print("hello python")
# # 对于没有返回值的函数,调用方法,直接函数名(参数)
# # len是有返回值的函数
# a = len("hello python")  # 会把一个值返回给调用者
# print(a)
# print(len("hello python"))

def my_sum(a, b):
    return a + b   # 把a + b 的结果,返回给调用者

num1 = my_sum(2, 3)  # 这里就是调用my_sum函数,所以num1得到了函数的返回值
print(num1)
print(my_sum(5, 6))