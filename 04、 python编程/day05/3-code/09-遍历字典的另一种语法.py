dict1 = {"name":"刘备", "age":20, "sex":"男"}
# for n in dict1.items():
#     print(n)
# 一旦使用了字典的items方法,n就是一个包含了键和值的元组
# n就是一个包含了两个成员的元组,第一个成员是键,第二个成员是值
# for循环了3次
# 第一次n = ('name', '刘备')
# 第二次n = ('age', 20)
# 第三次n = ('sex', '男')

# for n in dict1.items():
#     a, b = n  # 对一个元组进行拆包
#     print(a, b)

for a, b in dict1.items():  # a就是键,b就是键对应的值
    print(a, b)