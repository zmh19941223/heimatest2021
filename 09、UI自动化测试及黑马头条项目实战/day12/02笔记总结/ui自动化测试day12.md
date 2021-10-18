# ui自动化测试day12

## 一、日志收集

### 1、日志相关概念

日志的概念：日志就是用于记录系统运行时的信息，对一个事件的记录

#### 1.1 日志的作用

* 调试程序
* 可以用来判断程序是否运行正常
* 可以用来分析和定位问题
* 可以用来做用户行为分析和数据统计

#### 1.2 日志的级别

* 调试级别   DEBUG  记录的一些代码的调试信息
* 信息级别    INFO    记录一些正常的操作信息
* 警告级别     Warring  记录的是一些警告日志信息，但不会影响系统的功能及正常运行
* 错误级别    Error    记录的是系统运行时的错误信息，说明系统的某些功能不能正常运行
* 严重错误级别  critical  记录的系统运行时的严重错误信息，有可能导致整个系统都不能运行。



---

###  2、logging模块

logging是python自带的日志收集模块

#### 2.1 logging的基本用法

* 通过logging模块来输出日志信息.

  使用前需要导入logging模块

  使用方法： logging.debug("这是一条调试级别的日志")

  ​					logging.info("这是一条信息级别的日志")

  注意点：logging模块默认的级别是warring级别，默认的输出格式："   级别: root : 日志信息"

  如果设置了对应级别，那么会输出大于或等于对应级别的日志信息

  ```python
  #  导包
  import logging
  
  # 调用logging输出日志
  logging.debug("这是一条调试级别的日志")
  logging.info("这是一条信息级别的日志")
  logging.warning("这是一条警告级别的日志")
  logging.error("这是一条错误级别的日志")
  logging.critical("这是一条严重级别的日志")
  ```

  

#### 2.2 logging的日志级别设置

* 日志级别的设置:  logging.basicConfig(level=logging.DEBUG)

  日志级别的选择：

  开发环境和测试环境：可以使用DEBUG或者INFO级别都可以

  生产环境：建议使用WARRING或者EEROR

#### 2.3 logging的日志格式设置

* 日志格式设置：  logging.basciConfig(format=fmt)  # fmt表示的日志格式字符串

  ```python
  #  导包
  import logging
  # 定义一个格式化的字符串
  fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
# 设置日志的级别
  logging.basicConfig(level=logging.DEBUG, format=fmt)
  # 调用logging输出日志
  logging.debug("这是一条调试级别的日志")
  logging.info("这是一条信息级别的日志")
  logging.warning("这是一条警告级别的日志")
  logging.error("这是一条错误级别的日志")
  logging.critical("这是一条严重级别的日志")
  ```
  
  
  
  
  
  

#### 2.4 将日志输出到文件

* 将日志输出到文件：

  logging.basicConfig(filename = 'log/a.log')    # 日志文件保存的目录必须手动创建

如果将日志输出到文件当中，就不会在控制台打印出对应的日志信息了。

```python
#  导包
import logging
# 定义一个格式化的字符串
fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
# 设置日志的级别
logging.basicConfig(level=logging.DEBUG, format=fmt, filename='log/a.log')
# 调用logging输出日志
logging.debug("这是一条调试级别的日志")
logging.info("这是一条信息级别的日志")
logging.warning("这是一条警告级别的日志")
logging.error("这是一条错误级别的日志")
logging.critical("这是一条严重级别的日志")
```







### 3、logging的高级用法

#### 3.1 logging的四大组件介绍

* 四大组件

  * 日志器  logger   ：  是程序的入口，主要用来记录日志的信息

  * 处理器  handler ： 决定了日志的输出目的地
  * 格式器  formatter ：决定了日志的输出格式
  * 过滤器  filter： 决定哪些日志信息被输出，哪些被丢弃

  总结： 日志器是程序的入口，最终通过处理器来决定日志器该往哪里输出对应的日志信息

#### 3.2 logger类

* 创建日志器:   logger = logging.getLogger()   或者 logger = logging.getLogger("myLogger")

  如果创建的日志器不带参数，默认的日志名称是root

  如果创建的日志器带了参数，日志名称为对应的参数名

  如果创建的日志器名称相同，实际上，这两个日志器使用的是同一个日志名称。

  日志器常用方法:

  * 输出日志信息: logger.debug(msg)

    ​						logger.info(msg)

    ​						logger.warring(msg)

  * 设置日志的级别: logger.setLever(logging.INFO)

  * 添加处理器: logger.addHandler(handler)

#### 3.3 handler类

* 处理器的作用：决定日志输出到目的地
* 常用处理器类：
  * logging.StreamHandler    将日志信息输出到控制台
  * logging.hanlders.TimedRotatingFileHandler    将日志信息输出到文件，并支持按时间来切割

* 处理器类常用的方法
  * 设置日志的级别        handler.setLevel()
  * 在处理器当中添加格式器   handler.setFormatter()

```python
import logging
import logging.handlers
import time

logger = logging.getLogger("myLogger")  # 创建logger日志器
logger.setLevel(logging.DEBUG)  # 设置日志器的级别

# 创建 输出日志到文件的处理器， 文件按时间来切割的
handler = logging.handlers.TimedRotatingFileHandler("log/test.log", when='S', interval=30, backupCount=3)
handler.setLevel(logging.INFO)

# 将处理器添加到日志器
logger.addHandler(handler)
while True:
    #  输出日志信息
    time.sleep(2)
    logger.info("这是一条信息级别的日志!")

```



#### 3.4 formatter类

* 格式器： 用来格式化日志信息的格式

  创建格式：  formatter = logging.formatter(fmt=fmt)  # fmt参数表示的是格式化的字符串

  可以将格式器添加到处理器就可以了。

  



#### 3.5 将日志输出到控制台和文件中

```python
import logging
import logging.handlers

# 1、创建日志器
import time

logger = logging.getLogger()

# 2、设置日志器级别
logger.setLevel(logging.DEBUG)

# 3、创建两个处理器（输出到控制台以及输出到文件）
#     3.1 创建输出到控制台的处理器
sf = logging.StreamHandler()
#     3.2 创建输出到文件的处理器
hf = logging.handlers.TimedRotatingFileHandler("log/log.log", when='M', interval=1, backupCount=3)

# 4、设置级别
sf.setLevel(logging.INFO)
hf.setLevel(logging.INFO)

# 5、创建格式器
fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
formatter = logging.Formatter(fmt=fmt)

# 6、添加格式器到处理器当中
sf.setFormatter(formatter)
hf.setFormatter(formatter)

# 7、将处理器添加到日志器
logger.addHandler(sf)
logger.addHandler(hf)

# 8、输出日志信息
while True:
    time.sleep(3)
    logger.info("这是一条信息级别的日志")
    logging.warning("这是一条警告级别的日志")
```





