# 1.定义一个程序员类(coder) ，有两个方法,
# 分别为工作(work)方法，睡觉(sleep)方法
# class coder:
#     def work(self):
#         print("work")
#     def sleep(self):
#         print("sleep")
#
# c = coder()
# c.sleep()
# c.work()

# 2.定义一个程序员类, 有__init__方法,
# 在__init__方法中添加name, age, sex属性 ;
# 其中name属性的值为”张三”;
# sex属性的值为”男”;
# age属性的值为30;

# class coder:
#     def __init__(self):
#         self.name = "张三"
#         self.age = 30
#         self.sex = "男"
#
# c = coder()
# print(c.name)
# print(c.sex)
# print(c.age)
#
# 3. 为程序员类提供__del__方法,
# 在程序员类的实例对象销毁时,输出”再见程序员”
class coder:
    def __del__(self):
        print("再见程序员")

c = coder()