#!/usr/bin/env python3
#coding: utf-8

import smtplib,logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = 'shimengjie@senbaba.cn'
receiver ='tech@senbaba.cn'
subject='[森巴巴]接口自动化测试报告通知'
smtpserver='smtp.exmail.qq.com'
username='shimengjie@senbaba.cn'
password='242815smj'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot['From'] = sender
msgRoot['To'] = ''.join(receiver)
#构造附件
att = MIMEText(open('D:\\apache-jmeter-2.13\\apache-jmeter-2.13\\bin\\script\\testreport\\results\\test\\TestReport.html', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="TestReport.html"'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
logging.info(u"发送成功。")
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()