# a还是一个循环计数器
# b决定了循环的最大次数
a = 0
b = int(input("请输入b的值"))

while a < b:
    print("*")
    a += 1
    if a >= 20: # 不管b的值多大,一旦a到了20,循环就退出
        break