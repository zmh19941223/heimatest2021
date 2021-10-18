try:
    num1 = int(input("请输入num1的值"))
    num2 = int(input("请输入num2的值"))
    op1 = input("请输入op1的值")
    if op1 == "+":
        print(num1 + num2)
    elif op1 == "-":
        print(num1 - num2)
    elif op1 == "*":
        print(num1 * num2)
    elif op1 == "/":
        print(num1 / num2)
    else:
        print("op1值不对")
except ValueError:
    print("请输入一个可以转化整数")
except ZeroDivisionError:
    print("除数不能为0")
except:
    print("未知错误")
