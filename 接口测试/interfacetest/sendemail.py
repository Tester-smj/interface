#coding:utf-8
import configparser,os

def get_conf():
    conf_file = configparser.ConfigParser
    conf_file.read(os.path.join(os.getcwd(),'conf.ini'))
    conf = {}
    conf['sender'] = conf_file.get("email", "sender")
    conf['receiver'] = conf_file.get("email","receiver")
    conf['smtpserver'] = conf_file.get("email","smtpserver")
    conf['username'] = conf_file.get("email","username")
    conf['password'] = conf_file.get("email","password")
    return conf
