#coding=utf-8
import smtplib,logging
from email.mime.text import MIMEText
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