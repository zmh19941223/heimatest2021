str1 = "abcdefg"
str2 = str1[2:4:1]
print(str2)
str2 = str1[:4:1]
print(str2)
str2 = str1[2::1]
print(str2)
str2 = str1[2:4:]
print(str2)
# 从左往右数   0     1       2      3       4
list1 = ["刘备", "关羽", "张飞", "赵云", "马超"]
# 从右往左数-5      -4     -3     -2       -1
list2 = list1[2:4:]
print(list2)
list2 = list1[::2]
print(list2)