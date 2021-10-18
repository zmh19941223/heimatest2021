# 有文件a.txt
# 内容如下:
#
# 我爱你python, 我爱你
#
# 有文件b.txt
# 内容如下:
#
# hello
#
# 把文件a.txt和b.txt合并为c.txt
# 思路:把文件a.txt内如读出来放到变量a
# 把文件b.txt内如读出来放到变量b
# 把a + b 结果写入的c.txt中
file = open(r"c:\file\temp\a.txt", "r")
a = file.read()
file.close()
file = open(r"c:\file\temp\b.txt", "r")
b = file.read()
file.close()
file = open(r"c:\file\temp\c.txt", "w")
file.write(a + b)
file.close()