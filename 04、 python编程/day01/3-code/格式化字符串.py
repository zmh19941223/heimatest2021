name = "张三"
age = 20
print("姓名" + name + ", 年龄" + str(age) + "岁")
# 这两个print输入的结果是一样的
print("姓名%s, 年龄%d岁" % (name, age))
print("姓名%s, 年龄%d岁, %%, %%s" % (name, age))