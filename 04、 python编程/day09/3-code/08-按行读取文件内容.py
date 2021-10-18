file = open(r"c:\file\temp\a.txt", "r")
# 在循环开始的时候,不知道文件有多少行,所以也不能决定循环多少次
while True:
    txt = file.readline()
    # 如果readline读取到文件最后末尾,返回""
    if txt == "":
        break
    print(txt, end="")

file.close()