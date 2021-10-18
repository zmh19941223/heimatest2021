# file = open(r"c:\file\temp\a.txt", "r")
# txt = file.read()
# print(txt)
# file.close()
# 对等代码
with open(r"c:\file\temp\a.txt", "r") as file:
    txt = file.read()
    print(txt)