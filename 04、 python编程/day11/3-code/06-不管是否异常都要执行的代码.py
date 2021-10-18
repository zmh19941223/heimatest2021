try:
    a = int(input("请输入a的值"))
    b = int(input("请输入b的值"))
    print(a / b)
except:
    print("异常发生")
finally:
    print("不论是否有异常都要执行的代码")