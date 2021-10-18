import logging

logger = logging.getLogger("myLogger")  # 创建logger日志器
logger.setLevel(logging.DEBUG)  # 设置日志器的级别

# 创建 输出日志到控制台的处理器
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# 将处理器添加到日志器
logger.addHandler(handler)

#  输出日志信息
logger.info("这是一条信息级别的日志!")


