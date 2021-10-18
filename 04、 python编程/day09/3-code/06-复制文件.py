# 把文件a.txt复制为b.txt
# 思路:把a.txt打开,读取全部内容
# 把b.txt用w方法打开,把内容写入
file = open(r"c:\file\temp\a.txt", "r")
txt = file.read()
file.close()
file = open(r"c:\file\temp\b.txt", "w")
file.write(txt)
file.close()