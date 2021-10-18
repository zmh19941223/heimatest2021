import json
file = open("a.json", "r", encoding="utf8")
data = json.load(file) # 把json文件的内容转化为python的字典
file.close()
# print(data)
for n in data:
    print(n, data[n])