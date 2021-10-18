class animal:
    def sleep(self):
        print("睡")
    def eat(self):
        print("吃")

class dog(animal):  # 类dog继承自animal类
    def run(self):
        print("跑")

d = dog()   # dog会拥有animal所有属性和方法
d.sleep()
d.eat()
d.run()
