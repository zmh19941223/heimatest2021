class animal:
    def sleep(self):
        print("睡")

    def eat(self):
        print("吃")

class dog(animal):
    def run(self):
        print("跑")

class fish(animal):
    def swimming(self):
        print("游泳")

class bird(animal):
    def fly(self):
        print("飞")

b = bird()
b.sleep()
f = fish()
f.swimming()
