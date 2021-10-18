# 计算器,当用户输入的不是+-*/会抛出异常,并捕捉这个异常
try:
    num1 = int(input("请输入整数"))
    num2 = int(input("请输入整数"))
    op1 = input("请输入+-*/")
    if op1 != "+" and op1 != "-" and op1 != "*" and op1 != "/":
        raise Exception("请输入正确的+-*/")
    if op1 == "+":
        print(num1 + num2)
    elif op1 == "-":
        print(num1 - num2)
    elif op1 == "*":
        print(num1 * num2)
    else:
        print(num1 / num2)

except Exception as result:
    print(result)