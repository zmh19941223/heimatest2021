# 有个文件a.txt,内容每一行是一个整数,最大值和最小值的差
# 思路:
# 把文件每一行 做为list的每个成员(文件的每一行是字符串)
# 只有max(list) - min (list)
#
# 先做一个空的list
# 循环读每行,把每行用int转化为整数,append到空的list里面
# 循环读完后,就可以max(list) - min(list)
file = open(r"c:\file\temp\a.txt", "r")
list1 = []
while True:
    txt = file.readline()
    if txt == "":
        break
    list1.append(int(txt))
file.close()
print(max(list1) - min(list1))