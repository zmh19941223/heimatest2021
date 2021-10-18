选择题
1.[多选]:针对标签定位下面说法正确的是:    ABCD

```html
<body>
    <input type="text" class="inp fmobile J_cellphone" name="invite">
    <input class="inp fsecpass J_password2" id="password2" name="password2" >
</body>
```

A.使用driver.find_element_by_tag_name("input")可以定位第一个input元素；
B.使用driver.find_element_by_xpath("//input")可以定位第一个input元素；
C.不建议使用标签定位，因为一般情况下每个标签在页面中存在多个的可能性较大；
D.页面上所有的元素都有标签名。

2.[多选]:对于下面的元素，能成功定位a标签的表达式有哪些？ ABCDEF

```html
<body>
    <div class="item-left">
        <h3 class="cata-nav-name">
            <div class="cata-nav-wrap">
                <i class="ico ico-nav-1"></i>
                <a href="/Home/Goods/goodsList/id/2.html" title="家用电器">家用电器
                </a>
            </div>
        </h3>
    </div>
</body>
```

A.driver.find_element_by_link_text("家用电器")；
B.driver.find_element_by_partial_link_text("电器")
C.driver.find_element_by_tag_name("a")
D.driver.find_element_by_xpath("//a")
E.driver.find_element_by_xpath("//div/a")
F.driver.find_element_by_xpath("//**[@title='家用电器']")
G.driver.find_element_by_xpath("//\**[text()='家用']")

3.[多选]:对于xpath下面说法正确的是？  BCD
A.xpath是一种标记语言，可以用于在html中进行元素查找；
B.xpath可以使用标签内的任意元素来进行定位；
C.xpath可以基本解决所有元素定位的问题；
D.xpath定位方式将整个页面的所有元素进行扫描以定位我们所需要的元素，如果脚本中大量使用xpath做元素定位的话， 脚本的执行速度可能会稍慢。

4.[多选]:定位下面的元素，xpath路径定位策略表达式正确是？   ABD

```html
<body>
    <div id='testA'>
        <input type="text" class="inp fmobile J_cellphone" 		name="invite" id="password">
    </div>
</body>
```

A.//body/div/input
B.//input
C./div//input
D.//input[1]

5.[多选]:定位标签待付款，对于xpath属性定位表达式正确的是：ABCD

```html
<div class="navitems2 p" id="navitems5">
    <ul>
        <li>
        <a href="order_list.html" value="全部订单" class="selected">全部订单
        </a>
        </li>
        <li>
        <a href="WAITPAY.html" value="待付款" class="">待付款</a>
        </li>
        <li>
        <a href="WAITSEND.html" value="待发货" class="">待发货</a>
        </li>
    <ul>
</div>
```

A.//a[@value='待付款']
B.//\*[@value='待付款']
C.//a[@href='WAITPAY.html']
D.//\*[@value='待付款' and @href='WAITPAY.html']



6.[多选]:定位全部订单付款，对于xpath属性层级表达式正确的是：  ABC

```html
<div class="navitems2 p" id="navitems5">
    <ul class="tb1">
        <li id="table1">
            <a href="order_list.html" value="全部订单" class="selected">全部订单</a>
        </li>
    <ul>
</div>
```

A. //ul/li/a
B.//li/a
C.//li[@id='table1']/a
D.//ul[@class='tb1']/a[1]



7.[多选]:关于CSS说法正确的是：ABC
A.CSS定位相对xpath来讲的速度更快；
B.CSS定位时通过CSS选择器的模式来实现选择元素的；
C.CSS是用来描述HTML样式语言；
D.CSS不能定位一组元素；



8.[多选]:以下CSS表达式错误的是： BD

```html
<div class="navitems2 p" id="navitems5">
    <input id="testA" name="testA" value="all" class="selected">请输入		</input>
</div>
```

A.#testA
B.*testA
C. .selected
D.[@value='all']
E. input
F.input[value='all']



9.[多选]:通过CSS层级选择器能定位到标签元素的表达式有哪些：BCD

```html
<div class="p" id="navitems5">
    <div>
    	<div id="testA" name="testA" value="all"/>
    </div>
    <div id="demoA">
    	<input id="testA" name="testA" value="all" class="selected">请输入</input>
    </div>
</div>
```

A.div [@id='testA']
B.div>#testA
C.div[class='p'] input
D.#demoA .selected

10.下面关于元素定位说法错误是：D
A.driver.find_element_by_tag_name(‘input’)和driver.find_element_by_xpath("//input")定位结果一样；
B.driver.find_element_by_xpath("//input")和driver.find_element_by_css_selector("input")定位
结果一样；
C.CSS层级定位策略中层级选择器，空格表示法可以代替">"的表示法；
D.CSS可以定位到所有的元素；



编程题
1.在CSDN的网站中，请写出定位以下元素的xpath或者css表达式

```
1、找到 首页上方推荐列表中的“前端”（https://www.csdn.net/）

2、找到 首页中程序人生中的第二篇文章标题（https://www.csdn.net/）

3、找到 首页“热门推荐”中的第二篇文章标题（https://www.csdn.net/）

4、找到 首页中的“创作中心”按钮（https://www.csdn.net/）


```



2.按以下要求完成登陆流程：

```
#1.使用css定位定位tpshop首页登陆超链接，并执行点击
#2.使用id定位定位登陆页面用户名输入框，输入用户名
#3.使用name定位定位登陆页面密码输入框，输入密码
#4.使用class定位定位登陆页面验证码输入框，输入验证码
#5.使用xpath定位登陆按钮执行点击
#6.打印登陆后页面标题和地址信息
```



3.按以下要求完成注册流程：

```
#要求使用元素定位另外一种写法：driver.find_element(By.XXX,value)
#1.使用xpath的文本形式定位tpshop首页注册超链接，并点击
#2.使用css属性定位策略定位手机号码输入框，输入手机号码
#3.使用css属性包含的方式定位验证码输入框，输入验证码
#4.使用xpath属性与逻辑结合定位方式定位密码输入框，输入设置密码
#5.使用xpath路径定位策略定位确认密码，输入确认密码
#6.使用超链接定位方式定位同意协议并注册按钮，并点击
```

