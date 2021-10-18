# a = int(input("请输入一个整数"))
# b = int(input("请输入一个整数"))
str1 = input("请输入一个整数") # 不要着急转int,转int前先判断能不能转
str2 = input("请输入一个整数") # 不要着急转int,转int前先判断能不能转
if str1.isdigit() and str2.isdigit():
    a = int(str1)
    b = int(str2)
    print(a + b)
else:
    print("老实点,小心挨打")

# 如果用户老老实实,输入的是整数,就计算两个整数的相加结果
# 如果用户不老实,输入的是不是整数,就显示"老实点,小心挨打"

# 当一个函数或者方法返回值就是True或者False,在if条件后面只写方法名就好