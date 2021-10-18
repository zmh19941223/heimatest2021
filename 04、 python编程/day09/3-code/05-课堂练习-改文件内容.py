# 有文件a.txt
# 内容如下:
# 我爱你python, 我爱你
#
# 写代码,把a.txt内容中的python替换为world
#
# 思路,先把a.txt文件内用r方式读出来
# 用字符串的replace方法把python替换为world
# 在用w方式把替换后的内容写回到a.txt里面
file = open(r"c:\file\temp\a.txt", "r")
txt = file.read()
a = txt.replace("python", "world")
file.close()  # 这一步必须关闭
file = open(r"c:\file\temp\a.txt", "w")
file.write(a)
file.close()