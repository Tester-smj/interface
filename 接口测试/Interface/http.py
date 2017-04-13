# # #coding=utf-8
# #
# # class Myclass():
# #     name="sum"
# #
# #     def Sayhi(self):
# #         print('hello')
# #
# #
# # #实例化类
# # a=Myclass()
# # #调用类里面的方法
# # a.Sayhi()
# # coding: utf8
#
# # @Author: 郭 璞
# # @File: DLUTLibraryLogin.py
# # @Time: 2017/4/7
# # @Contact: 1064319632@qq.com
# # @blog: http://blog.csdn.net/marksinoberg
# # @Description: 大连理工大学图书馆模拟登陆,添加了验证码识别脚本
#
# import BeautifulSoup
# import pytesseract
# import requests.sessions
# from PIL import Image
#
# loginurl = 'http://opac.lib.dlut.edu.cn/reader/redr_verify.php'
# captchaurl = 'http://opac.lib.dlut.edu.cn/reader/captcha.php'
#
# headers = {
#     'Referer': 'http://opac.lib.dlut.edu.cn/reader/login.php',
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
# }
#
# s= requests.Session()
# ##### 获取到验证码并保存
# checkcodecontent = s.get(captchaurl, headers=headers)
#
# with open('checkcode.jpg', 'wb') as f:
#     f.write(checkcodecontent.content)
#     f.close()
# print('验证码已写入到本地！', '下面开始调用tesseract-OCR引擎识别验证码！')
#
# img = Image.open('checkcode.jpg', mode='r')
# result = pytesseract.image_to_string(image=img)
# checkcode = result
# print('验证码为：', checkcode)
#
# # os.startfile('checkcode.jpg')
# # checkcode = input('请输入验证码：')
# ##### 准备登陆图书馆系统
# payload = {
#     'number':'学号',
#     'passwd':'密码',
#     'captcha': checkcode,
#     'select':'cert_no'
# }
#
# response = s.post(loginurl, headers=headers, data=payload)
# print('服务器端返回码： ', response.status_code)
# soup = BeautifulSoup(response.text, 'html.parser')
# ## 打印当前用户
# username = soup.find('font', {'color': 'blue'})
# print(username.get_text())
# ## 打印积分信息
# jifen = soup.find_all('span', {'class': 'bigger-170'})[3]
# jifen = str(jifen.get_text())
# print('当前登录用户总积分：', jifen)
#coding:utf-8
from selenium import webdriver
# a=dict['Chrome','Firefox']
browser = webdriver.Firefox()
base_url = "http://www.senbaba.cn"
browser.get(base_url)
browser.maximize_window()
try:
    browser.save_screenshot("F:\\BugP\\chrome.png")
except:
    print("error")
browser.close()
