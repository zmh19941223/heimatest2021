list1 = ['刘备', '关羽', '张飞']
list1.insert(1, '吕布')
list1.append("曹操")
print(list1)
list2 = ['周瑜', '孙权']
list1.extend(list2)  # 把list2的所有成员,追加到list1的后面
print(list1)
list1[1] = '许褚'  # 修改第二个成员的值
print(list1)
del(list1[4])
print(list1)
list1.remove('张飞')
print(list1)
list1.pop()
print(list1)
list1.pop(0)  # 删除索引为0的成员
print(list1)
list1.clear()
print(list1)

list1 = ['刘备', '关羽', '张飞', '刘备', '关羽']
print(list1.count('刘备'))
print(list1.count('张飞'))
print(list1.count('吕布'))
print(list1.index('刘备'))
list1 = [4, 3, 1, 56, 12, 67]
# list1.sort()
# list1.sort(reverse=True)
list1.reverse()
print(list1)
