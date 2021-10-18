# 定义字符串变量 name = “小明”，输出: 我的名字叫小明，请多多关照！
name = "小明"
print("我的名字叫%s，请多多关照！" % name)
# 2. 定义整数变量 num = 1，输出: 我的学号是 000001
num = 1
print("我的学号是 %06d" % num)
# 3. 定义⼩数 price = 8.5、 weight = 5 ，输出：苹果单价 8.5 元／⽄，购买了 5.00 ⽄，需要支付 42.50 元
price = 8.5
weight = 5
print("苹果单价 %.1f元／⽄，购买了 %.2f ⽄，需要支付 %.2f 元" % (price, weight, price * weight))
# 4. 定义⼀个⼩数 scale = 10.01 ，输出: 数据是 10.01%
scale = 10.01
print("数据是 %.2f%%" % scale)