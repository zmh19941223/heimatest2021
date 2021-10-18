# 一个print只能输出一个星号
# *
# **
# ***
num1 = 0
while num1 < 3:
    a = 0
    while a <= num1:
        print("*", end="")
        a += 1
    print()
    num1 += 1