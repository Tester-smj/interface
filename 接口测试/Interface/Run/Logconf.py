#coding=utf-8
import os,logging
def log_save():
    #保存log
    log_file = os.path.join(os.getcwd(),'sas.log')
    log_format = '[%(asctime)s] [%(levelname)s] %(message)s'     #配置log格式
    logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter(log_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)