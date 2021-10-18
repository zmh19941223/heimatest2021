try:
    a = int(input("请输入a的值"))
    b = int(input("请输入b的值"))
    print(a / b)
except ValueError:
    print("请输入正确的整数")
except ZeroDivisionError:
    print("除数不能为0")
except Exception as result:
    print("未知异常", result)
else:
    print("代码没有异常发生")
finally:
    print("代码执行完成")