import logging
import logging.handlers
from common import contants
#debug   info    warn   error   critical   五种错误类型

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel("INFO")
    #顶一个输出格式
    fmt = "%(asctime)s - %(name)s- %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]"
    format = logging.Formatter(fmt)

    file_handler = logging.handlers.RotatingFileHandler(contants.log_dir,maxBytes=20*1024*1024,backupCount=10,encoding='utf-8')# 新建一个日志文件
    #设置输出级别
    file_handler.setLevel("INFO")
    file_handler.setFormatter(format)

    #添加格式
    logger.addHandler(file_handler)
    return logger
# get_logger("invest").setLevel("INFO")
# get_logger("invest").error("这是一个错误")
# get_logger("invest").info("这是一个提示信息")
