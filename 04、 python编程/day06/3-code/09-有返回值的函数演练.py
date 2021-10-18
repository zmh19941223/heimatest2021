def my_func1(start, stop):
    sum = 0
    a = start
    while a <= stop:
        sum += a
        a += 1
    return sum

num1 = my_func1(4, 10)
print(num1)
