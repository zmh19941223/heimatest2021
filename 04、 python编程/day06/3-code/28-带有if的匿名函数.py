# def my_max(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# num1 = my_max(4, 5)
num1 = (lambda a, b : a if a > b else b)(4, 5)
print(num1)