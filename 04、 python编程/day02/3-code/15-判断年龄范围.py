age = int(input("请输入年龄"))
if age < 10 and age > 0:
    print("小孩")
elif age >= 10 and age < 20:
    print("小朋友")
elif age >= 20 and age < 30:
    print("年轻人")
elif age >= 30 and age < 50:
    print("中年人")
elif age >= 50:
    print("老年人")
else:
    print("年龄不对")
