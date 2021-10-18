def my_squar(height, width):
    return height * width

a = my_squar(3, 4) # 定义一个变量a,得到调用my_squar函数的返回值
print(a)

def my_func(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

print(my_func(8, 4))
print(my_func(9, 4))