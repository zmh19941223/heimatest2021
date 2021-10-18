name = input("请输入姓名")
if name == "tom":
    age = int(input("请输入年龄"))
    if age >= 30:
        print("大叔")
    else:
        print("小弟")
else:
    print("姓名错误")