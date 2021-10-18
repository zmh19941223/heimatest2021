# list1是列表变量名, 列表中有三个成员
list1 = ['关羽', '曹操', '刘备']
print(list1[0])
print(list1[1])
print(list1[2])
# print(list1[3])  # 显示第四个成员, 如果显示一个列表没有的成员,会出错

list2 = []   # 定义了一个空列表变量叫list2
# print(list2[0])  # 对于空列表,不能访问成员

print(dir(list1))