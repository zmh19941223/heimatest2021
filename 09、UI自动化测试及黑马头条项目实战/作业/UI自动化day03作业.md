# web自动化day03作业

选择题  
1.[多选]通过自动化脚本获取元素信息的目的有哪些？ AB 
A.web自动化测试是通过程序来代替手工验证系统功能是否和预期结果一致的过程，那么就需要通过自动化脚本来获取界面上面相关元素信息来做实际结果和预期结果做比对；
B.获取元素信息可以作为其它脚本所需要的参数；
C.获取元素



2.[多选]以下获取元素信息的常用方法说法正确的是？ ABC
A.验证商品详情页商品图片规格大小是否符合需求规格说明书，可以使用element.size来获取图片大小；
B.验证注册协议是否默认勾选，可以使用element.is_selected来判断元素是否是勾选状态；
C.当在窗口上点击某功能后跳转或页面更新成新的信息，可以通过element.text获取比较个性的元
素文本信息来判断跳转或功能处理是否正确；
D.element.get_attribute("value")可以获取元素内属性值信息，方法中的value为属性值。

3.下面哪个为实例化鼠标操作的方法？  B
A.action = ActionChains()；
B.aciton = ActionChains(driver)；
C.action = actionChains(driver)；
D.action = actionChains()；

4.[多选]下面常用鼠标操作方法和说明正确匹配的是:  ACD
A.action.double_click(element) -- 双击；
B.action.context_click(element) -- 左键单击；
C.action.move_to_element(element) -- 悬停；
D.action.perform() # 执行鼠标操作；

5.[多选]元素对象send_keys方法用途包含: ABCD 
A.模拟键盘组合键操作element.send_keys(Keys.键符,'字母键')；
B.对于上传文件控件，如是input标签，可以直接通过element.send_keys("文件完整路径")来进行上传；
C.模拟键盘特殊按键操作element.send_keys(Keys.键符)；
D.模拟文本输入element.send_keys("字符串")

6.关于元素等待下面说法错误的是:  D
A.元素等待就是在定位页面元素时如果未找到，会在指定时间内一直等待的过程；
B.元素等待包括隐式等待、显式等待、强制等待；
C.网络速度慢、电脑配置低、服务器处理请求慢都会引起网页加载缓慢，从而导致元素定位不到；
D.使用元素等待可以加快元素加载的速度；

7.关于隐式等待下面说法错误的是:  A
A.隐式等待对其设置前的元素定位也会执行等待过程；
B.隐式等待对该设置后所有元素定位都生效，都会执行等待过程；
C.隐式等待在超过最大时长后如果未找到对应元素，则会抛出异常:NoSuchElementException；
D.隐式等待的默认查找元素的间隔时长为0.5s,超时时长一般设置10~30秒；

8.关于显式等待下面说法错误的是:  A
A.显式等待对该设置后所有元素定位都生效，都会执行等待过程；
B.显式等待只针对其WebDriverWait(driver, 10, 1).until(lambda x:
x.find_element_by_xxx("value")方法中所定位指定元素生效；
C.显式等待在超过最大时长后如果未找到对应元素，则会抛出异常：TimeoutException；
D.执行显式等待的方法如能定位到元素，最终返回的是元素对象；
E.显式等待需要导包WebDriverWait；

9.[多选]:观察下面元素对象，请选择说法正确的选项： ABCE

```html
<select id='subject'>
    <option value='java'>java</option>
    <option value='c++'>c++</option>
    <option value='test'>test</option>
</select>
```

A.select+option标签形式为html原生态下拉框选择形式，selnium提供了专门Select类来进行操作；
B.Select(driver.find_element_by_id('subject')).select_by_index(1)可以选中c++；
C.Select对象提供了select_by_value(value)的方法来选择选项，value表示option选项的value值；
D.Select(driver.find_element_by_css_selector(”[value='test']"))可以选中test；
E.select标签下拉框同样也可以使用元素定位并点击的方式来实现选择操作；

10.以下关于弹出框说法错误的是：A
A.所有界面弹出框都不能直接进行元素定位来实现对其操作；
B.通过js实现的弹出框形式，在触发后，如不做处理其它元素都不能进行操作；
C.通过js实现的弹出框实现方式常用三种形式为:alert 警告框、confirm 确认框、prompt提示框；
D.通过js实现的弹出框形式都不能通过元素定位的方式进行定位；

编程题
1.Select下拉框操作脚本步骤？

2.弹出框操作脚本实现步骤？

3.按以下要求完成操作流程(定位方式不限)：

```
1.进入tpshop首页并登陆
2.循环打印会员首页的会员折扣、可用积分、账户余额、优惠券信息
3.在会员首页顶部的搜索引擎中输入小米，点击搜索
4.使用悬停的方式到购物车的中获取商品数量以及总金额，需要用到判断条件，判断是否为空。
```





