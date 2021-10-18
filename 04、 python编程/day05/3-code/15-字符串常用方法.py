str1 = "abcde123fg"
print(str1[3])
print(str1[-1])
print(str1[-3])
if str1.isalpha():
    print("字符串都是由字母构成的")

str2 = "1234ab5"
if str2.isdigit():
    print("str2是由纯数字组成的")