tuple1 = ('刘备', '关羽', '张飞')
a = tuple1[1]
print(a)
# tuple1[1] = '曹操'  # 元组的值不能修改
print(tuple1.count('刘备'))
print(tuple1.index('刘备'))
tuple2 = (4, 6, 1, 67, 100)
print(len(tuple2))
print(max(tuple2))
print(min(tuple2))
if 3 in tuple2:
    print("3在元组tuple2中")