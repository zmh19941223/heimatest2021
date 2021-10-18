list1 = ['张飞', 3, 4.5, '曹操']
a = 1
for n in list1:
    print("列表第%d个成员的值是%s" % (a, str(n)))
    a += 1

sum = 0
list1 = [56, '32', 45, '6']
for n in list1:
    sum += int(n)
print(sum)