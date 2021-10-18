str1 = "123 98 234 23 345"
# 思路,先把str1中每个数字分隔出来
list1 = str1.split(" ")
# 遍历列表,计算和
sum = 0
for n in list1:
    sum += int(n)    # n的类型为字符串,所以需要转化为int
print(sum)