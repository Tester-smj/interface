# -*- coding: utf-8 -*-
import unittest
import json
import requests,sys,HTMLTestRunner,logging,os,time

url="http://www.senbaba.cn"
urltest="http://120.24.68.124:8080/sbborders"
class TestCode(unittest.TestCase):
    def setUp(self):
        # 把所需要的一些初始准备数据全都在setUp写好
        # 测试URL参数化
        self.url=urltest
        global headers,cookies
        self.data ={"uname":"187071484771","pwd":"123456"}
        r=requests.post(self.url+"/login",self.data)
        headers = {'content-type': 'application/json',
                   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                   'Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
                   'Accept-Language':'zh-CN'}
        #cookies直接去登录成功后服务端返回的header
        cookies=r.headers
        logging.info(r.text)

    def test_getprice(self):
        u"""获取价格"""
        self.data={"car_struct_name": "商务",
                   "newcapacity": "5",
                   "etBeginTime": "2026-07-16 15:55:00",
                   "etFinishTime": "2026-07-16 15:55:09",
                   "vehicleCount": "1",
                   "tdays": "0",
                   "fromCity": "深圳市",
                   "departurePlace": "深圳北站",
                   "toCity": "深圳市",
                   "destinationPlace": "深圳皇岗口岸",
                   "tagValue": "",
                   "tripValue": "",
                   "cost": "140",
                   "contractName": "test",
                   "contractPhone": "18707148477",
                   "remark": "script",
                   "contr_select_bus_info": "0",
                   "couponName": "",
                   "departureCoords": "{'area':',广州市,越秀区,','coords':[23.155001,113.264057],'name':'广州火车站'}",
                   "destinationCoords": "{'area':'广东省,深圳市,福田区,福田南路,','coords':[22.615102,114.035529],'name':'深圳皇岗口岸'}",
                   "pathway": "[]",
                   "jobType": "0",
                   "withTolls": "0",
                   "addItion": "0"}
        a=requests.get(self.url+"/getprice",self.data,cookies=cookies,headers=headers)
        print(a.text)
        #解码json格式数据
        dicts=json.loads(a.text)
        code=a.status_code
        #对比返回值
        self.assertEqual(code,200)
        self.assertEqual(dicts['status'],'ok')
        self.assertEqual(dicts['error'],None)

    def test_addorder(self):
        u"""多辆车不议价包销下单"""
        self.data={"car_struct_name":"商务",
                   "newcapacity":"5",
                   "etBeginTime":"2026-07-16 15:55:00",
                   "etFinishTime":"2026-07-16 15:55:09",
                   "vehicleCount":"1",
                   "tdays":"0",
                   "fromCity":"深圳市",
                   "departurePlace":"深圳北站",
                   "toCity":"深圳市","destinationPlace":"深圳皇岗口岸",
                   "tagValue":"",
                   "tripValue":"",
                   "cost":"620",
                   "contractName":"test",
                   "contractPhone":"18707148477",
                   "remark":"script",
                   "contr_select_bus_info":"0",
                   "couponName":"",
                   "departureCoords":"{'area':',广州市,越秀区,','coords':[23.155001,113.264057],'name':'广州火车站'}",
                   "destinationCoords":"{'area':'广东省,深圳市,福田区,福田南路,','coords':[22.615102,114.035529],'name':'深圳皇岗口岸'}",
                   "pathway":"[]",
                   "content":"[{'key':'driver_info','name':'司机业务属性','values':[]},{'key':'bus_info','name':'车辆新旧程度','values':{'name':'全部','value':'0'}}]",
                   "jobType":"0",
                   "confirm":"0",
                   "days":"0",
                   "tripNo":"",
                   "withTolls":"0",
                   "addItion":"0",
                   "count":"1",
                   "couponCode":"",
                   "fleetCode":"",
                   "fleetName":""}
        z=requests.get(self.url+'/addorder',self.data,headers=headers,cookies=cookies)
        #解码json格式数据
        a=z.text
        print(z.text)
        dicts=json.loads(z.text)
        print dicts["data"]
        code=z.status_code
        #对比返回值
        self.assertEqual(code,200)
        self.assertEqual(dicts['status'],'ok')
        self.assertEqual(dicts['error'],None)

    def test_cancleorder(self):
        u'''取消订单'''
        self.data={"car_struct_name":"商务",
                   "newcapacity":"5",
                   "etBeginTime":"2026-07-16 15:55:00",
                   "etFinishTime":"2026-07-16 15:55:09",
                   "vehicleCount":"1",
                   "tdays":"0",
                   "fromCity":"深圳市",
                   "departurePlace":"深圳北站",
                   "toCity":"深圳市","destinationPlace":"深圳皇岗口岸",
                   "tagValue":"",
                   "tripValue":"",
                   "cost":"620",
                   "contractName":"test",
                   "contractPhone":"18707148477",
                   "remark":"script",
                   "contr_select_bus_info":"0",
                   "couponName":"",
                   "departureCoords":"{'area':',广州市,越秀区,','coords':[23.155001,113.264057],'name':'广州火车站'}",
                   "destinationCoords":"{'area':'广东省,深圳市,福田区,福田南路,','coords':[22.615102,114.035529],'name':'深圳皇岗口岸'}",
                   "pathway":"[]",
                   "content":"[{'key':'driver_info','name':'司机业务属性','values':[]},{'key':'bus_info','name':'车辆新旧程度','values':{'name':'全部','value':'0'}}]",
                   "jobType":"0",
                   "confirm":"0",
                   "days":"0",
                   "tripNo":"",
                   "withTolls":"0",
                   "addItion":"0",
                   "count":"1",
                   "couponCode":"",
                   "fleetCode":"",
                   "fleetName":""}
        z=requests.get(self.url+'/addorder',self.data,headers=headers,cookies=cookies)
        #解码json格式数据
        print(z.text)
        dicts=json.loads(z.text)
        a=dicts['data']
        self.url=urltest+"/cancleorder"
        self.data={"reasons":"[{'cancelReason':'天气原因导致行程改变或取消','cancelType':6}]","orderid":a['orderNo']}
        asd=requests.get(self.url,self.data,cookies=cookies,headers=headers)
        print(asd.text)
        #解码订单取消接口json格式数据
        dicts1=json.loads(asd.text)
        print dicts1["data"]
        code=z.status_code
        data1=dicts1['data']
        tip=data1['tips']
        #对比返回值
        self.assertEqual(code,200)
        self.assertEqual(dicts['status'],'ok')
        self.assertEqual(dicts['error'],None)
        self.assertEqual(data1['tips'],u'订单已取消')

    def tearDown(self):
        pass

def CurrentPath():
    current_path=os.getcwd()
    print ('current path: ',current_path)
    project_path=os.path.dirname(current_path)
    print "project path:",project_path

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    #这块是获取项目路径，后面在生成report时会放到改目录下
    current_path=os.getcwd()
    print ('current path: ',current_path)
    project_path=os.path.dirname(current_path)
    print "project path:",project_path
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCode("test_getprice"))
    suite.addTest(TestCode("test_addorder"))
    suite.addTest(TestCode("test_cancleorder"))
    #定义date为日期，time为时间
    date=time.strftime("%Y%m%d")
    time=time.strftime("%Y%m%d%H%M%S")
    # filedir=project_path+"//report//"+temp
    # os.makedirs(filedir)
    # filename="//pyresult.html"
    # filepath=filedir+filename
    #创建路径
    path='F:/test/'+date+"/"
    os.makedirs(path)
    filename=path+'report.html'
    fp=file(filename,'wb')
    #执行测试
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'下单平台接口测试用例',description=u'接口用例列表：')
    runner.run(suite)
    fp.close()
