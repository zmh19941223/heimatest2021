# ['刘备', '诸葛亮', '曹操', '周瑜', '关羽']
# 作业,把列表中个成员名字逆序
# 把列表中也逆序
list1 = ['刘备', '诸葛亮', '曹操', '周瑜', '关羽']
list1 = list1[::-1]   # 把列表中的成员逆置
# print(list1)
# 列表中每个字符串也要逆置
# 思路,遍历列表,在遍历出来每个字符串后,把每个字符串逆置
index = 0   # 定义了一个变量叫index,值为0
for n in list1:
    str1 = n[::-1]  # str1就是n颠倒后的结果
    list1[index] = str1
    # 第一次循环的时候index的值为0,所以相当于list1[0] = str1
    # 第二次循环的时候index的值为1,所以相当于list1[1] = str1
    index += 1
print(list1)
