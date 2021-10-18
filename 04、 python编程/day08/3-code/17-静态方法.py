class dog:
    @staticmethod
    def help():
        print("这是一个静态方法")

class A:
    @staticmethod
    def help():
        print("这是第二个静态方法help")

dog.help()
A.help()