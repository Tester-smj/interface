#coding:utf-8 
import xlrd
import requests
import os,time

def apidata(xls):
    data = xlrd.open_workbook(xls)
    table = data.sheets()[0]
    nrows = table.nrows     #获取行数
    print(nrows)
    ncols = table.ncols     #获取列数
    print(ncols)
    url = table.cell(1,2).value     #获取URL
    api = table.cell(2,2).value
    req = table.cell(3,2).value     #获取接口方式
    print(api)
    print(url)
    print(req)
    data = []
    data1 = {}
    for i in range(nrows):      #循环获取行值
        try:
            apinaeme = table.cell(i+1,0).value      #获取参数名
            print(nrows,i,apinaeme)
            apiname1 = apinaeme.encode("utf-8")
            if apiname1 == "end" or apiname1 =="":
                print("读取到end，进行参数调整！")
                data.append(data1)
                data1={}
                print(data1,data)
                continue
            apidata = table.cell(i+1,1).value       #获取参数的值
#             print(apidata)
            apidata1 = apidata.encode("utf-8")
            data1[apinaeme] = apidata1
        except Exception:
            pass
        print("获取接口参数成功！")
        return data,url,req         #返回参数以及URL

def log(r1,t1):     #保存值到本地
   x = time.strftime("%Y-%m-%d",time.localtime())
   x1 = t1+x+".txt"
   fo = open(x1,"w+",encoding='utf-8')
   print(x1)
   #r2 = r1.encode("utf-8")
   fo.write(r1)

xls = os.path.join(os.getcwd(),'Book1.xlsx')
api,url,ruq = apidata(xls)
print(api)
print(type(api))
print(url)
print(ruq)

def requtest(api,url,ruq):
    if ruq == 'post':
        r = requests.post(url,api)
    elif ruq == 'get':
        r = requests.get(url,api)
    else:
        print("没有设置协议类型，请先设置！")
    # print(r.text)
    # print("接口请求成功！")
    return r

num = 0
for j in (api):
    num = num + 1
    y1 = ""
    y1 = "第"+str(num)+"请求数据："+str(j)+"\n"
#     print(y1)
    log(y1,"test")
    x = requests(j,url,ruq)
    # x1 = eval(x.text)
    y2 = ""
    y2 = "第"+str(num)+"返回参数："+str(x.json())+"\n"
    log(y2,"test")
    if x.ok:
        print("第",num,"次接口请求成功！")
        x1 = x.json()
        # print(x1['OutputData'])
        x2 = x1['OutputData'][0]['Success']
        # x3 = x2[0]['Data'][0]['Success']
        if x2 == "True":
            print("第",num,"接口返回参数正确！")
        else:
            print("第",num,"接口返回参数错误，请检查日志！")
    else:
        print("第",num,"接口请求失败！")
print("本次用例执行完成，详情信息请查看日志文件！")          