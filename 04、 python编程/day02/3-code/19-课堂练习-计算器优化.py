num1 = int(input("请输入num1的值"))
num2 = int(input("请输入num2的值"))
a = input("请输入a的值")
if a == "+":
    print(num1 + num2)
elif a == "-":
    print(num1 - num2)
elif a == "*":
    print(num1 * num2)
elif a == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("除数不能为0")
else:
    print("a的值必须为+-*/")