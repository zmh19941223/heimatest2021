# ui自动化测试day11

## 一、PO模式

### 3、V3版本

#### 3.1 方法封装



#### 3.2 V3版本代码实现

缺点：1、 如果前端页面的元素信息发生了变更，那么自动化代码就需要去更新元素，而且是只要用到了这个元素就都要去更新。维护不方便

2、针对登录的代码，存大大量的冗余。



### 4、V4版本实现

#### 4.1 PO模式介绍

PO是page  object的简称，核心思想是通过对界面元素的封装减少冗余代码，同时在后期维护中，若元素定位发生变化， 只
需要调整页面元素封装的代码，提高测试用例的可维护性、可读性。

PO模式可以把一个页面分为三层，对象库层、操作层、业务层。
对象库层：封装定位元素的方法。
操作层：封装对元素的操作。
业务层：将一个或多个操作组合起来完成一个业务功能。比如登录：需要输入帐号、密码、点
击登录三个操作。

注意点：

1、确认需要操作的页面

2、每个页面所需要用到的元素对象

#### 4.2 PO模式优点

减少冗余代码
业务代码和测试代码被分开，降低耦合性
维护成本低

#### 4.3 PO模式实现



V4版本缺点：

1、元素定位的信息，如果页面元素过多，不方便维护

2、如果输入前没有做清除操作，代码的健壮性不够好。





### 5、V5版本（PO模式优化）

缺点：

1、元素定位，针对元素定位，没有使用显示等待。

2、代码的健壮性不够。



### 6、V6版本（PO模式的深入封装）

1、针对元素定位封装到操作的基类当中，且是通过显示等待来进行元素定位

2、针对元素输入之前做了清除的操作。封装在操作层的基类当中。



## 二、数据驱动

### 1、数据驱动介绍

概念：通过测试数据来驱动测试用例的执行。

#### 1.1 数据驱动特点

* 数据驱动本身不是一个工业级标准的概念，因此在不同的公司都会有不同的解释。
* 可以把数据驱动理解为一种模式或者一种思想。
* 数据驱动技术可以将用户把关注点放在对测试数据的构建和维护上，而不是直接维护脚本，可
  以利用同样的过程对不同的数据输入进行测试。
* 数据驱动的实现要依赖参数化的技术。

#### 1.2 数据驱动方式

* 直接定义在测试脚本中（简单直观，但代码和数据未实现真正的分离，不方便后期维护）
* 从文件读取数据，如JSON、excel、xml、txt等格式文件
* 从数据库中读取数据
* 直接调用接口获取数据源
* 本地封装一些生成数据的方法

#### 1.3 json读取文件回顾



### 2、数据驱动实战一



### 3、数据驱动实战二



