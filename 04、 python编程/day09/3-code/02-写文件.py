# 第一步:打开文件
file = open(r"c:\file\temp\b.txt", "w")
# 第二步:写内容
file.write("hello python")
# 第三步:关闭文件
file.close()
# 验证程序是否执行成功?看c盘file目录的temp目录下是否生成了文件b.txt
# b.txt文件内容是否为hello python