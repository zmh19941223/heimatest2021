list1 = ['张飞', '刘备', '关羽', '刘邦', '刘老二', '曹操']
if "刘备" in list1:
    list1.remove("刘备")
print(list1)

list2 = [3, 5, 67, 2, 34, 12, 5, 11]
# 求列表的平均值
# 求平均值就是先求和,然后除以成员数量
sum = 0
for n in list2:
    sum += n
print(sum / len(list2))