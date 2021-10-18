try:
    a = int(input("请输入a的值"))
    b = int(input("请输入b的值"))
    print(a / b)
except:
    print("异常发生")
else:
    print("没有异常发生")