list1 = ['张三', '李四', '刘老二', '王麻子', '隔壁老王']
# 写代码判断列表中名字为三个字的人有几个
sum = 0
for n in list1:
    if len(n) == 3:
        sum += 1
print(sum)