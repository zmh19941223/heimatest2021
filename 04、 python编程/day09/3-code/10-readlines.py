file = open(r"c:\file\temp\a.txt", "r")
list1 = file.readlines()
for n in list1:
    print(n, end="")
file.close()