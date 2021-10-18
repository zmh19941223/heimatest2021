# 1:石头
# 2:剪刀
# 3:布
# 石头赢剪刀
# 剪刀赢布
# 布赢石头
# 人通过键盘输入石头,剪刀,和布
# 电脑随机产生数字1或者2或者3
# 如果电脑产生数字1,那么就要转化为石头
# 如果电脑产生数字2,那么就要转化为剪刀
# 如果电脑产生数字3,那么就要转化为布

# 比较胜负
import random
# pc代表电脑要出的拳,可能是1,可能2或者3
pc = random.randint(1, 3)
# 需要把数字1,2,3转化为对应的字符串
# 变量a存放数字转化为字符串的结果
a = None
if pc == 1:
    a = "石头"
elif pc == 2:
    a = "剪刀"
else:
    a = "布"

# player代表人要出的拳,可能是石头或者剪刀或者布
player = input("请输入石头或者剪刀或者布")

if (a == "石头" and player == "剪刀") or (a == "剪刀" and player == "布") or (a == "布" and player == "石头"):
    print("电脑出了%s, 我出了%s, 电脑赢了" % (a, player))
elif (a == player):
    print("电脑出了%s, 我出了%s, 平局" % (a, player))
else:
    print("电脑出了%s, 我出了%s, 我赢了" % (a, player))