list1 = ['刘备', '关羽', '张飞']
tuple1 = ('曹操',  '周瑜')
list1.extend(tuple1)   # 改变的是list1,tuple1没有改变
print(list1)
print(tuple1)
list1[3] = '张三'
print(list1)
print(tuple1)