# 有文件a.txt,有很多行,只显示偶数行
# 思路:只读方式打开a.txt,读取所有行,但只显示偶数行
# 做一个循环读取所有行,在循环的时候做一个计数器,每次循环计数器+1
# 可以判断计数器是偶数还是奇数,如果是偶数那么就print

file = open(r"c:\file\temp\a.txt", "r")
index = 1
while True:
    txt = file.readline()
    if txt == "":
        break
    if index % 2 == 0:  # 如果条件成立,代表index为偶数
        print(txt, end="")
    index += 1

file.close()
