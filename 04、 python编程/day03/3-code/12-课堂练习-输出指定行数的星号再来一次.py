# 如果输出3行星号
# a = 0
# b = 3
# while a < b:
#     print("*")
#     a += 1
# 如果b的值不是代码写死的,是通过input输入的
a = 0
b = int(input("请输入b的值"))  # 假设用户输入了数字10
while a < b:
    print("*")
    a += 1   # 在循环内部,a的值一直在变化,但b的值从来不变
    if a >= 20:
        break