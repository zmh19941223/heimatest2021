a = 0
while a < 5:
    if a == 3:
        continue  # a等于3的时候,就再也没机会执行a += 1这个代码了
    print(a)
    a += 1