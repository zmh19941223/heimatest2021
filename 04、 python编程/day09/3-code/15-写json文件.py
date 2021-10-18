import json
dict1 = {"name":"刘备", "age":20, "sex":"男"}
file = open("data.json", "w", encoding="utf8")
json.dump(dict1, file, ensure_ascii=False)
file.close()