选择题
1、[多选]为什么要执行自动化测试？    ABC
A.降低项目成本，保障软件质量；
B.节省测试周期时间；
C.提高软件质量的准确性和可靠性；
D.自动化测试可以代替手工测试；

2、[多选]下面哪些场景需要或者可以通过自动化进行测试？   AB
A.某web网站上线后，每天的平均在线用户超过1000w，出现系统经常崩溃的情况；
B.某web网站需要保障chrome、Firefox、ie8/9/10、360、Safari等多达10种浏览器能正常使用；
C.某web网站首页广告图经常更换，且需要验证图片显示内容；
D.某web网站界面交互、风格主题调整版本上线。

3、[多选]自动化测试有哪些种类？ ABCD  
A.web自动化测试；
B.移动自动化测试；
C.接口自动化测试；
D.单元测试；
4、[多选]web自动化测试按是否查看代码代码划分属于哪个类型的测试？ CD 
A.灰盒测试；
B.白盒测试；
C.黑盒测试；
D.功能测试；

5、web自动化测试可以在以下哪些阶段开始？  A 
A.功能测试完毕后；
B.集成测试完毕后；
C.冒烟测试完毕后；
D.以上都可；

6、[多选]通常情况下，挑选web自动化测试工具的依据有哪些？  ABC
A.为了节省成本，优先挑选开源测试工具；
B.基于公司平台所需要支持浏览器种类，尽量挑选支持浏览器多的测试工具；
C.挑选市场上使用比较多的且功能比较强大的测试工具；
D.在无基础的情况下挑选一款学习成本较大且不稳定的新测试工具；

7、[多选]selenium3.0的核心组件有哪些？  ABC
A.Grid；
B.IDE；
C.WebDriver；
D.RC；

8、[多选]对下面代码描述正确的是：  ABCD

```python
from selenium import webdvier
driver = webdriver.Chrome()
```

A.selenium对于python解释器来讲属于第三方模块；
B.driver表示一个谷歌浏览器驱动对象实例；
C.driver单词可以更换为test_driver；
D.driver是变量；

9、对于下面代码使用的元素定位方式正确的是： A

```html
<body>
	<input id="username" name="userA" />
	<input id="username" name class="testA testB testC"/>
	<div id="demoA">
		<span>测试</span>
	</div>
</body>
```

A.第一个input标签可以直接使用driver.find_element_by_id('username')定位；
B.第二个input标签可以直接使用driver.find_element_by_id('username')定位；
C.标签可以直接使用id定位；
D.第二个input标签可以使用driver.find_element_by_class_name("testB testC")定位；

10、[多选]对于编写web自动化脚本习惯下面描述错误的是：AD
A.自动化脚本文件可以使用"-"、"空格"、"/"命名；
B.在使用id、name、class_name定位时所传递的参数值尽量到浏览器开发者工具中找到该元素后
拷贝对应的值；
C.养成编写注释信息的习惯；
D.使用常见第三方模块来命名文件，如导包导了webdriver包，新增脚本的时候使用webdriver命名。



编程题
1、如何搭建selenium自动化测试环境？

```

```



2、selenium脚本编写基本步骤？

```

```



3、使用元素定位方法完成tpshop注册?

```

```

