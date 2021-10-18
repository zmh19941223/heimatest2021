# 1代表坦克
# 2代表飞机
# 3代表大炮
import random
a = random.randint(1, 3)
if a == 1:
    print("坦克")
elif a == 2:
    print("飞机")
else:
    print("大炮")