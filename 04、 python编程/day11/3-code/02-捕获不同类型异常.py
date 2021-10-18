try:
    a = int(input("请输入一个整数"))
    b = int(input("请输入一个整数"))
    print(a / b)
except ValueError:
    print("请输入一个可以转化整数")
except ZeroDivisionError:
    print("除数不能为0")
except:
    print("未知错误")

# ValueError: 输入的值不能转化为整数
# ZeroDivisionError: 除数为0的时候报的错误
