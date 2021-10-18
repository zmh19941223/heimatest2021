# 在模块中__init__.py的作用是，导入当前模块时，默认运行的文件
# 所以后续，只要import api 或者 from api import xxx，就会运行api下的__init__.py中的代码
# 就会进行日志的初始化，初始化后就可以使用logging模块来打印日志，例如：logging.info("日志消息")

# 初始化日志
import logging
import utils

utils.init_logging() # 初始化日志

# 测试初始化日志的结果
logging.info("测试在api下的__init__.py中的日志打印结果！")