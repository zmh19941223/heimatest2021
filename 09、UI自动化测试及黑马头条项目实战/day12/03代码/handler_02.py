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


