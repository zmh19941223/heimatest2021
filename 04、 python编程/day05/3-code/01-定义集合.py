set1 = {'刘备', '关羽', '张飞'} # 定义了一个集合变量set1
set2 = set()   # 定义一个空集合set2
set3 = {'刘备', '关羽', '刘备'}
print(set1)
print(set2)
print(set3)

set1.add('曹操')
print(set1)
# set1.pop()
print(set1)
set1.remove('刘备')
print(set1)
set1.clear()
print(set1)