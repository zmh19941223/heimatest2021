# 思路:
# 先把内容从test.json文件中读出来
# 读出来的结果是一个字典
# 把字典中键age对应 的值修改为30
# 再把字典写回到test.json文件中
import json
file = open("test.json", "r", encoding="utf8")
dict1 = json.load(file)
file.close()
dict1["age"] = 30
file = open("test.json", "w", encoding="utf8")
json.dump(dict1, file, ensure_ascii=False)
file.close()