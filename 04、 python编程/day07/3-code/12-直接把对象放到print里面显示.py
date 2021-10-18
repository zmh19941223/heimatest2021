class cat:
    def __init__(self):
        pass

c = cat()
print(c)  # 当把对象直接放到print里面,实现的是对象在内存的地址编号
# 有时候,我们希望print能显示我们想显示的内容

# 假设,自己设计一个对象,放到print里面,显示对象的name属性值
class demo:
    def __init__(self, name = "demo"):
        self.name = name

    def __str__(self):
        return self.name

d = demo()
print(d)