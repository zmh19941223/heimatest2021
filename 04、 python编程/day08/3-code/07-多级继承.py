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

class erha(dog):
    def kawayi(self):
        print("萌")

class cangao(dog):
    def yaoren(self):
        print("咬人")

class shark(fish):
    def chiren(self):
        print("吃人")

s = shark()
s.sleep()
s.eat()
s.swimming()
s.chiren()

c = cangao()
c.sleep()
c.eat()
c.run()
c.yaoren()