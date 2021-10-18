# 导入utils.py中编写的初始化日志的函数和logging模块
# 然后调用初始化日志的函数
# 最后测试日志是不是能够打印

# 导包
import utils
import logging

# 初始化日志
utils.init_logging()

# 使用logging模块打印日志
logging.info("Test初始化日志后能不能打印日志")