list1 = [4, 2, 5, 3]
print(len(list1))
str1 = "hello"
print(len(str1))
list1 = ['刘备','关羽','张飞']
print(len(list1))
# 如果len里面放的是列表,返回列表成员的个数
# 如果len里面放的是字符串,返回字符串中字符的个数

list1 = [54, 12, 78, 123, 77]
print(max(list1))
str2 = "hellaz"
print(max(str2))
list2 = ['abc', 'bcd', 'edf']
print(max(list2))

print(min(list1))
print(min(str2))
print(min(list2))

list3 = [4, 6, 1, 23]
if 4 in list3:
    print("有4")

if 5 not in list3:
    print("没有5")

str3 = "hello"
if "a" in str3:
    print("有a")

if "b" not in str3:
    print("没有b")