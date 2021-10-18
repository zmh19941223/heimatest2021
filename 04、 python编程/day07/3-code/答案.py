# [{'name':'刘备', 'age':20}, {'name':'关羽', 'age':30}, {'name':'张飞', 'age':27}]
# 查找年龄最大的人的姓名

list1 = [{'name':'刘备', 'age':20}, {'name':'关羽', 'age':30}, {'name':'张飞', 'age':27}]
list2 = []
for n in list1:
    list2.append(n['age'])

num = max(list2)

for n in list1:
    if n['age'] == num:
        print(n['name'])
