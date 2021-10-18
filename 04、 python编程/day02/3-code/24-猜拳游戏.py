# 1:石头
# 2:剪刀
# 3:布
# 石头赢剪刀  1赢2
# 剪刀赢布    2赢3
# 布赢石头    3赢1
# 人通过键盘输入数字1或者2或者3
# 电脑随机产生数字1或者2或者3
# 比较胜负
import random
# pc代表电脑要出的拳,可能是1,可能2或者3
pc = random.randint(1, 3)
# player代表人要出的拳,可能是1或者2或者3
player = int(input("请输入1或者2或者3"))
if (pc == 1 and player == 2) or (pc == 2 and player == 3) or (pc == 3 and player == 1):
    print("电脑出了%d, 我出了%d电脑赢了" % (pc, player))
elif (pc == player):
    print("电脑出了%d, 我出了%d, 平局" % (pc, player))
else:
    print("电脑出了%d, 我出了%d,我赢了" % (pc, player))