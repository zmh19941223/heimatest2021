# 外循环循环了5次
# 内循环循环了5次
# 内循环的print("*", end="")
# 每次内循环完成外循环都有个print()
for a in range(0, 5):
    for b in range(0, 5):
        print("*", end="")
    print()