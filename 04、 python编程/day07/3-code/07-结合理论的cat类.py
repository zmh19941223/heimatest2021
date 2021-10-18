class cat:
    def __init__(self, name = "tom", color = "red"):
        self.name = name
        self.color = color

    def show_name(self):
        print(self.name)

    def show_color(self):
        print(self.color)

    def show(self):
        self.show_name()
        self.show_color()

c1 = cat("小猫", "white")
c1.show_name()
c1.show_color()
c2 = cat("大猫", "black")
c2.show_name()
c2.show_color()
c3 = cat()
c4 = cat("懒猫")
