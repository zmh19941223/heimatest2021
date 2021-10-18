class cat:  # 定义了一个类cat,这个类不能直接使用
    def eat(self):  # 第一个参数必须是self
        print("猫吃饭")
    def drink(self):
        print("猫喝水")

c1 = cat()   # 根据类cat, 创建了一个对象c1, 对象名类似于变量名
c1.eat()  # 调用的时候,不需要提供self对应的实参
c1.drink()  # 调用对象的方法
# 方法只能通过对象调用,不能通过类直接调用
# c1就是类cat的实例
# c1 = cat() 这个动作就叫实例化
c2 = cat()   # 实例化, 实例化的结果是cat类有一个对象叫c2
# c2是类cat的实例