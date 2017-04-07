#!usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    # 'Cookie':'CNZZDATA1260535040=242528197-1478672438-null%7C1478672438',
}
url= 'http://www.beiwo.tv/index.php?s=vod-search-id-14-tid--area--year-$search_year-order-gold.html'

wb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
imgs = soup.select(" ul.img-list.clearfix > li > a > img ")
titles = soup.select(" ul.img-list.clearfix > li > h5 ")
yanyuans = soup.select(" ul.img-list.clearfix > li > p")
stars = soup.select(" p.star > em")

J_data = {}
count = 0
for title,img,yanyuan,star in zip(titles,imgs,yanyuans,stars):
    data = {
        "title":title.get_text(),
        "img":img.get("src"),
        "演员":list(yanyuan.stripped_strings),
        "评分":star.get_text(),
    }
    J_data[count] = data
    count += 1
    print(data)

with open("test.txt",'r') as f:
    dic=json.loads(f.readline())

for i in range(len(dic)):
    print(dic[str(i)])