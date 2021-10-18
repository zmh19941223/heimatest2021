
# 第一步: 打开文件
file = open(r"C:\file\temp\a.txt", "r")
# 第二步:读取文件内容
txt = file.read()
print(txt)
# 第三步:关闭文件
file.close()