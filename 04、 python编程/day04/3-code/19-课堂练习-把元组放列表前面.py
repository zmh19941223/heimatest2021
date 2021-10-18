list1 = ['刘备', '关羽', '张飞']
tuple1 = ('曹操',  '周瑜')
# list1.insert(0, tuple1)
# print(list1)
# for n in tuple1:
#     list1.insert(0, n)
# print(list1)
# for第一次循环的时候,n的值是曹操
# insert的时候,曹操是第一个成员
# for第二次循环的时候,n的值是周瑜
# insert的时候,周瑜是第一个成员

# 第一次循环的时候,把n放到0这个位置
# 第二次循环的时候,把n放到1这个位置
a = 0
for n in tuple1:
    list1.insert(a, n)
    a += 1
# 第一次循环a的值为0insert(0, 曹操)
# 第二次循环a的值为1insert(1, 周瑜)
print(list1)