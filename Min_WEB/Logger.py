import logging
# 创建logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 创建hander 用于写入日志文件
logfile = './log.txt'
fh = logging.FileHandler(logfile, mode='a')
fh.setLevel(logging.DEBUG)  # 输出file的log等级开关
# 再创建一个handler，用于输出控制台

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# 定义handler的输出格式

formater = logging.Formatter(
    '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
fh.setFormatter(formater)
ch.setFormatter(formater)

# jianglogger添加到handler中
logger.addHandler(fh)
logger.addHandler(ch)

# 日志
logging.debug("this is debug")
logging.info("this is info")
logging.warning("this is warning")
logging.error("****this is error***")
logging.critical("***this is critical***")
