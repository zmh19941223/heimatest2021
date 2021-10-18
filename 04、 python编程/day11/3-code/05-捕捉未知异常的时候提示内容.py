try:
    a = int(input("请输入a的值"))
    b = int(input("请输入b的值"))
    print(a / b)
except Exception as result: # 捕捉未知异常,把未知异常系统的错误提示显示出来
    print(result)