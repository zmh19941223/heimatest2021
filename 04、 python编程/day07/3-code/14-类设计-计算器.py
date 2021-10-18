class calc:
    def __init__(self, oper = "+"):
        self.oper = oper

    def calc(self, a, b):
        if self.oper == "+":
            return a + b
        elif self.oper == "-":
            return a - b
        elif self.oper == "*":
            return a * b
        elif self.oper == "/":
            if b != 0:
                return a / b
            else:
                return None
        else:
            return None

c = calc()
print(c.calc(3, 4))

d = calc("*")
print(d.calc(3, 4))

e = calc("/")
print(e.calc(3, 0))

f = calc("sdfsd")
print(f.calc(4, 5))