#coding=utf-8
import xlrd,os,requests,logging
import sys,json,re
xlsfile1 = os.path.join(os.getcwd(),'testCaseFile.xlsx')
#保存log
log_file = os.path.join(os.getcwd(),'log/sas.log')
log_format = '[%(asctime)s] [%(levelname)s] %(message)s'     #配置log格式
logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
def excel_data(xlsfile):
  #读取测试用例
  xlsfile1 = os.path.join(os.getcwd(),'testCaseFile.xlsx')
  if not os.path.exists(xlsfile1):
    logging.error('测试用例文件不存在！')
    sys.exit()
  book = xlrd.open_workbook(xlsfile)
  api_sheet = book.sheet_by_index(0)
  nrows = api_sheet.nrows
  #用于保存接口返回的内容和HTTP状态码
  errorCase = []
  #遍历用例
  for i in range(1,nrows):
    num = api_sheet.cell(i,0).value
    api_purpose = api_sheet.cell(i,1).value
    api_host = api_sheet.cell(i,2).value
    request_url = api_sheet.cell(i,3).value
    method=api_sheet.cell(i,4).value
    check_point = api_sheet.cell(i, 8).value
    data=api_sheet.cell(i,6).value
    url= api_host+request_url
    headers = {'content-type': 'application/json',
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
               'Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
               'Accept-Language':'zh-CN'}
    cookies = {'Transfer-Encoding': 'chunked',
             'Set-Cookie': 'JSESSIONID=826812B2F458375E7642892FCD0C649B; Path=/sbborders/; HttpOnly, sidd=7421BEEDAE6F253D15DB775C6FD2871E; Expires=Mon, 25-Jul-2016 10:23:07 GMT',
             'Content-Type': 'application/json;charset=utf-8',
             'Date': 'Fri, 15 Jul 2016 10:23:07 GMT',
             'Server': 'Apache-Coyote/1.1'}
    #字符串强转字典类型
    tata1=eval(data)
    # print(type(data))
    # print(type(tata1))
    if method == 'Post':
      z=requests.post(url,tata1,headers=headers)
    else :
      z=requests.get(url,tata1,headers=headers,cookies=cookies)
    status =z.status_code
    resp = z.text
    # print(z.cookies)
    if status != 200 or check_point not in resp :
      #如果状态码不为200,那么证明接口产生错误，保存错误信息。
      errorCase.append((api_purpose, str(status), api_host+request_url,resp ))
      logging.info(u'用例编号'+str(num) + u'执行结果是:'+u'失败，返回code是' + str(status) + ', ')
      logging.warn(z.text)
    else:
      logging.info(u'用例编号'+str(num) + u'执行结果是:' + u'成功！返回code是' + str(status) + ', ')
      logging.warn(z.text)
  return errorCase
    # if request_url=='/login':
    #     # print(z.cookies)
    #     print(z.headers)
    #     # json转换编码格式
    #     # a=z.json()
    #     # new=json.dumps(a,ensure_ascii=False)
    #     cookies1=z.cookies
    #     b=re.findall("{(.+?)}",str(z.headers))
    #     # print(new)
    #     # print(b)
    #     print(type(b))
    #     print(type(z.headers))
from email.mime.text import MIMEText
import smtplib,ConfigParser
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# def get_conf():
#     conf_file = ConfigParser.ConfigParser()
#
#     conf_file.read(os.path.join(os.getcwd(),'conf.ini'))
#
#     conf = {}
#
#     conf['sender'] = conf_file.get("email","sender")
#
#     conf['receiver'] = conf_file.get("email","receiver")
#
#     conf['smtpserver'] = conf_file.get("email","smtpserver")
#
#     conf['username'] = conf_file.get("email","username")
#
#     conf['password'] = conf_file.get("email","password")
#
#     return conf

def sendMail(text):
      # mail_info = get_conf()
      # sender = mail_info['sender']
      # receiver = mail_info['receiver']
      # subject = '[AutomationTest]接口自动化测试报告通知'
      # smtpserver = mail_info['smtpserver']
      # username = mail_info['username']
      # password = mail_info['password']
      sender = 'shimengjie@senbaba.cn'
      receiver ='shimengjie@senbaba.cn'
      subject='[下单平台]接口自动化测试报告通知'
      smtpserver='smtp.exmail.qq.com'
      username='shimengjie@senbaba.cn'
      password='242815smj'

      msg = MIMEText(text,'html','utf-8')
      msg['Subject'] = subject

      msg['From'] = sender
      msg['To'] = ''.join(receiver)

      smtp = smtplib.SMTP()
      smtp.connect(smtpserver)
      smtp.login(username, password)
      logging.info(u'邮件发送成功！')
      smtp.sendmail(sender, receiver, msg.as_string())
      smtp.quit()
def main():
      errorTest = excel_data(xlsfile1)
      if len(errorTest) > 0:
          html = '<html><body>接口自动化扫描，共有 ' + str(len(errorTest)) + '个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;text-align:left">接口</th><th style="width:50px;text-align:left">状态</th><th style="width:200px;text-align:left">接口地址</th><th   style="text-align:left">接口返回值</th></tr>'
          for test in errorTest:
              html = html + '<tr><td style="text-align:left">' + test[0] + '</td><td style="text-align:left">' + test[1] + '</td><td style="text-align:left">' + test[2]+'</td><td style="text-align:left">' + test[3]+'</td></tr>'
          sendMail(html)
      else:
          logging.info(u"无执行失败用例！")
      # print(len(errorTest))
if __name__=="__main__":
    main()