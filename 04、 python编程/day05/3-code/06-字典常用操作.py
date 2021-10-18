dict1 = {"name":"刘备", "age":20, "sex":"男"}
dict1["name"] = "关羽"  # 修改键name对应的值
print(dict1)
dict1["class"] = '1班'   # 新增一个键值对,键为class,值为1班
print(dict1)
dict1.pop('name')   # 删除name键,一旦键被删除,对应的值也同时被删除
print(dict1)
# dict1.clear()
print(dict1)
a = dict1["age"]  # 得到键对应的值
print(a)
b = dict1["sex"]  # 得到键sex对应的值
print(b)