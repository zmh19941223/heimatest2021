class animal:
    def food(self):
        pass
    def eat(self):
        self.food()

class dog(animal):
    def food(self):
        print("吃肉")

class cattle(animal):
    def food(self):
        print("吃草")

d = dog()
d.eat()
c = cattle()
c.eat()