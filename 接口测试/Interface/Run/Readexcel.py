#coding=utf-8
import os,logging,sys,xlrd,requests
def excel_data(xlsfile):
  #读取测试用例
  # xlsfile1 = os.path.join(os.getcwd(),'testCaseFile.xlsx')
  if not os.path.exists(xlsfile):
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
             'Set-Cookie': 'JSESSIONID=0E08C5A822EFA6819E364A5CA11A049C; Path=/sbborders/; HttpOnly, sidd=0E08C5A822EFA6819E364A5CA11A049C; Expires=Mon, 25-Jul-2016 10:23:07 GMT',
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