#coding:utf-8
import xlrd,logging,os
import sys,requests

testCaseFile1 = os.path.join(os.getcwd(),'TestCase/testCaseFile1.xlsx')
log_file = os.path.join(os.getcwd(),'log/error.log')
log_format = '[%(asctime)s] [%(levelname)s] %(message)s'
logging.basicConfig(format=log_format,filename=log_file,filemode='w',level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def runTest(testCaseFile):
    testCaseFile = os.path.join(os.getcwd(),'TestCase/testCaseFile1.xlsx')
    if not os.path.exists(testCaseFile):
        logging.error('测试用例文件不存在！')
        sys.exit()
    testCase = xlrd.open_workbook(testCaseFile)
    table = testCase.sheet_by_index(0)
    errorCase = []                      #用于保存接口返回的内容和http状态码
    
    for i in range(1,table.nrows):
        # if table.cell(i,9).value.replace('\n','').replace('\r','')!='Yes':
        #     continue
        num = table.cell(i,0).value
        api_purpose = table.cell(i,1).value
        api_host = table.cell(i,2).value
        request_url =table.cell(i,3).value
        request_data = table.cell(i,6).value
        url = api_host + request_url
        print(url)
        req = requests.get(url,request_data)
        status = req.status_code
        if status == 200:
            logging.info('用例编号'+str(num)+'执行结果是：成功，返回code是：'+str(status)+'\n')
        else:
            logging.info('用例编号'+str(num)+'执行结果是：失败，返回code是：'+str(status)+'\n')

if __name__ == "__main__":
    runTest(testCaseFile1)