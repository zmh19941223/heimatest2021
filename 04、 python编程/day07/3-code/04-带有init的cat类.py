class cat:
    def __init__(self):
        print("cat被创建了")
    def eat(self):
        print("小猫爱吃鱼")

c = cat()  # 实例化对象的时候,init方法自动调用
c.eat()  # 必须明确的通过代码调用普通方法