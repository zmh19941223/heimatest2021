# 如果while后面的条件为True,这个while就是一个人为的循环
# 循环内部一定要有if结合break来让循环退出的机制
while True:
    str1 = input("请输入一个字符串")
    if str1 == "exit":
        break
    print(str1)