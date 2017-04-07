#coding:utf-8
import requests

pqyload = {'q':'杨彦星'}
r = requests.get('http://www.so.com/s',params = pqyload)
r.url
