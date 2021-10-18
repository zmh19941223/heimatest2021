#  导包
import logging
# 设置日志的级别
logging.basicConfig(level=logging.DEBUG)
# 调用logging输出日志
logging.debug("这是一条调试级别的日志")
logging.info("这是一条信息级别的日志")
logging.warning("这是一条警告级别的日志")
logging.error("这是一条错误级别的日志")
logging.critical("这是一条严重级别的日志")