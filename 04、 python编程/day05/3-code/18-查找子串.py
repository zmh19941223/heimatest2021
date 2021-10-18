str1 = "hello python"
a = str1.find("python")
print(a)
a = str1.find("asffsf")
print(a)
str2 = str1.replace("python", "world")
# 并不是str1改变了,是把str1中的python变为world给str2了
# str1的值并没有改变
print(str2)

str3 = "hello world hello python"
a = str3.count("hello")
print(a)
a = str3.count("a")
print(a)