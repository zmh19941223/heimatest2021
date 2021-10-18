# 导入app.py全局变量文件
import app
import logging
from logging import handlers

# 定义初始化日志的函数
def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 创建文件处理器
    fh = logging.handlers.TimedRotatingFileHandler(app.BASE_DIR+"/log/mimi.log",
                                                   when='M',
                                                   interval=5,
                                                   backupCount=3,
                                                   encoding='utf-8')
    # 定义日志的格式(格式化器)
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)