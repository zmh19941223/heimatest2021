class animal:
    def sleep(self):
        print("睡")

    def eat(self):
        print("吃")

class dog(animal):
    def run(self):
        print("跑")

class erha(dog):
    def kawayi(self):
        print("萌")

e = erha()
e.sleep()
e.eat()
e.run()
e.kawayi()