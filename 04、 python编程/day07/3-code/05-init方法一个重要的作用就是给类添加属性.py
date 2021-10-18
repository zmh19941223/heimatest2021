# class cat:  # 不在普通方法中定义属性
#     def set_name(self, name):
#         self.name = name
#     def show_name(self):
#         print(self.name)
class cat:
    def __init__(self, name = "tom"):
        self.name = name
    def set_name(self, name):
        self.name = name
    def show_name(self):
        print(self.name)

c = cat("张三")  # init自动已经调用了,所以name属性已经有了
c.show_name()