#coding=utf-8
import logging,sys
import os
import Readexcel
import Sendemail
import Logconf
#解决编码格式问题导致邮件无法发送
reload(sys)
sys.setdefaultencoding('utf8')
xlsfile1 = os.path.join(os.getcwd(),'testCaseFile.xlsx')
def main():
    #调用方法
    Logconf.log_save()
    errorTest = Readexcel.excel_data(xlsfile1)
    if len(errorTest) > 0:
        html = '<html><body>接口扫描共有 ' + str(len(errorTest)) + '个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;text-align:left">接口</th><th style="width:50px;text-align:left">状态</th><th style="width:200px;text-align:left">接口地址</th><th   style="text-align:left">接口返回值</th></tr>'
        for test in errorTest:
            html = html + '<tr><td style="text-align:left">' + test[0] + '</td><td style="text-align:left">' + test[1] + '</td><td style="text-align:left">' + test[2]+'</td><td style="text-align:left">' + test[3]+'</td></tr>'
        # Sendemail.sendMail(html)
    else:
        logging.info(u"无执行失败用例！")
if __name__=="__main__":
    main()