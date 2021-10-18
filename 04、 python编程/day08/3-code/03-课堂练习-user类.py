class user:
    def __init__(self):
        self.name = "tom"
        self.__passwd = "123456"

    def show_name(self):
        print(self.name)

    def __show_passwd(self):
        print(self.__passwd)

u = user()
u.show_name()
# u.__show_passwd()  类的外部不能访问类的私有属性和方法