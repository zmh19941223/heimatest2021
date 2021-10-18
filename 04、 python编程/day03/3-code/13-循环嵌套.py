# ***
# ***

# 一个print只输出一个星号, 如何输出连续的三个星号
num1 = 0
while num1 < 2:  # 外循环一共循环2次,每次外循环的时候,内循环循环3次
    a = 0
    while a < 3:
        print("*", end="")
        a += 1
    print()  # 输出一个空的回车换行
    num1 += 1
print("end")

