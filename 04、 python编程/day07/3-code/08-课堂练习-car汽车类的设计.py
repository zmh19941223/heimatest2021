# 汽车car       要区分属性和方法,在init方法中为每个属性定义默认值
# 属性
# luntai(轮胎)
# yanse(颜色)
# chuanghu(窗户)
# xinghao(型号)
# 方法
# guadang(挂挡)
# qianjin(前进)
# houtui(后退)
# wurenjiashi(无人驾驶)
# shache(刹车)
# jiayou(加油)

class car:
    def __init__(self, luntai="轮胎", yanse="白色", chuanghu="黑窗户", xinghao="大众"):
        self.luntai = luntai
        self.yanse = yanse
        self.chuanghu = chuanghu
        self.xinghao = xinghao

    def guadang(self, a = "前进"):
        self.jiayou()
        if a == "前进":
            self.qianjin()
        elif a == "后退":
            self.houtui()
        else:
            print("档不对")

    def qianjin(self):
        print("%s在前进" % self.xinghao)
    def houtui(self):
        print("%s在后退" % self.xinghao)
    def wurenjiashi(self):
        print("无人驾驶")
    def shache(self):
        print("刹车")
    def jiayou(self):
        print("加油")

c = car()
# c.qianjin()
c.guadang("前进")

c1 = car(xinghao="奔驰")
c1.guadang("后退")