#coding='UTF-8'
import time
import logging

logging.basicConfig(level=logging.WARNING,filename='./log',filemode='a',format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logging.debug("this is debug")
logging.info("this is info")
logging.warning("this is warning")
logging.error("****this is error***")
logging.critical("***this is critical***")
