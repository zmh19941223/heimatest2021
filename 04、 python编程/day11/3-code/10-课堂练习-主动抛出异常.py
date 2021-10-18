# 设计一个函数,如果参数str1中有数字返回true,否则返回false
def digital(str1):
    for n in str1:
        if n >= "0" and n <= "9":
            return True
    return False

try:
    name = input("请输入姓名")
    if digital(name): # 条件成立,抛出异常
        raise Exception("名字不允许有数字")
    age = int(input("请输入年龄"))
    if age < 0:
        raise Exception("年龄不能小于0")
except Exception as result:
    print(result)


