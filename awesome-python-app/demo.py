# ecoding=utf-8
# print "heihei";
# temp=input("输入数字:")
# guess=int(temp)
# if guess == 8:
#     print("fuck")
# else:
#     print("heihei")
# print("gameover")
# a= "1234.25"
# b=3
# b -= 2
# print(b)
# b=b+1
# print(b)
# print(type(a),type(False));
# c= 3>4<5
# print(c)
# def Method():
#     print("123")
# Method()
# a=range(1,100)
# b=sum(a)
# print(b)
# array = [1,2,3,6,5,4]
# def bubble_sort(array):
#     for i in range(len(array)):
#         for j in range(i+1,len(array)):
#             if array[i] > array[j]:
#                 array[i],array[j]=array[j],array[i]
#
#         print array
# bubble_sort(array)
# def good(xuqiu):
#     print(xuqiu+2)
# good(2)
# list1=[2,3,34,0,9,7]
# list1.sort()
# print(list1)
# class Mylist(list):
#     pass
# list2=Mylist()
# list2.append(5)
# list2.append(3)
# print(list2)
# class Ball:
#     def setName(self,name):
#             self.name=name
#     def kick(self):
#             print("谁%s"% self.name)
# a=Ball()
# a.setName("A")
# b=Ball()
# b.setName("B")
# c=Ball()
# c.setName("C")
# a.kick()
# c.kick()
# b.kick()
# a=lambda x:2*x+1
# a(2)
# print(a(2))
# b=lambda x,y:x+y
# b1=b(2,y=1)
# print(b1)
# def old(x):
#     return x % 2
# #余2
# temp = range(10)
# show=filter(old,temp)
# list(show)
# print(list(show))
# print list(filter(lambda x:x % 2,range(10)))
# print(list(map(lambda x:x-1,range(10))))
# def factorial(n):
#     result=n
#     for i in range(1,n):
#         result=result*i
#     return result
# print(factorial(4))
# a=range(100)
# print sum(a)

# def factorials(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorials(n-1)
# print(factorials(4))
# import sys
# def recursion():
#     return recursion()
# print(sys.setrecursion())
# a=path.split(".")[-1]
import os
path="D:/cc.adb.txt"
def GetFileName(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return shotname
# print(GetFileName(path))

# b='aa.bb.cc'
# a=b.split(".")[:-1]
# c='.'.join(a)
# print(c)
#
# def factorial(n):
#     result = n
#     for i in range(1,n):
#         result*=i
#     return result
# print(factorial(3))

#迭代
def factor(n):
    n1=1
    n2=1
    n3=1
    if n < 1:
        print("null")
        return -1
    while(n-2)>0:
        n3 = n1+n2
        n1 = n2
        n2 = n3
        n-=1
    return n3
result=factor(40)
# print(result)
#递归
def factors(n):
    if n < 1:
        print("error")

    if n==1 or n==2:
        return 1
    else:
        return factors(n-1)+factors(n-2)
# print(factors(40))

#汉诺塔
# def hanoi(n,x,y,z):
#     if n == 1:
#         print(x,'-->',z)
#     else:
#         hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
#         print(x,'-->',z)#将最低下的最后一个盘子从x移动到z上
#         #将y上的n-1个盘子移动到z上
#         hanoi(n-1,y,x,z)
# n = int(input("pls:"))
# hanoi(n,'x','y','z')
dict1=dict({'a':1,'b':2})
# print dict1
dict2={}
a=dict2.fromkeys((1,3,2))
c=a.get(4,'asd')
b=dict2.fromkeys((1,2,3),'number')
d=b.copy()
e=[1,2,3,4,5,5,4,3,2,1,0]
temp=[]
for each in e:
    if each not in temp:
        temp.append(each)
f=list(set(e))
# print temp
g = open('D:\\adb.txt')
h=g.tell()
# print f,'\r\n',g,'\r\n',h


# import random,easygui
# a=random.randint(1,5)
# # print(a)
# try:
#     print(1+'1')
#     print(2/0)
#     print(int('a'))
# except ZeroDivisionError as reason:
#     print('文件出错啦\n错误的原因是：'+str(reason))
# except TypeError as reason:
#     print('文件出错啦\n错误的原因是：'+str(reason))
# try:
#     print(2/0)
# finally:
#     print(3/3)
# import random,easygui
# a=random.randint(1,5)
# easygui.msgbox("a")
# import easygui as g
# import sys
#
# while 1:
#     g.msgbox("hello world")
#
#     msg = "first python programe"
#     title = 'New Gui'
#     choices =['game','music','movie']
#
#     choice=g.choicebox(msg,title,choices)
#     g.msgbox("your choice is:"+str(choice))
#     msg='do u want to play again?'
#     title =  'pls choice'
#
#     if g.ccbox(msg,title):
#         pass
#     else:
#         sys.exit(0)
class Title:#首字母大写
    #定义属性
    name='大石'
    age='18'
    high='180cm'
    weight='75KG'

    #定义方法
    def Technolegy(self):
        print("test,python,jmeter,selenium")
#实例化对象
a=Title()
# print Title.name,a.Technolegy()

class Parent:
    def hello(self):
        print("正在调用父类方法")

class Child(Parent):
    def hello(self):
        print("正在调用子类的方法")
# p=Parent()
# p.hello()
# c=Child()
# c.hello()
import random
class Fish:
    def __init__(self):
        self.x=random.randint(0,10)
        self.y=random.randint(0,10)
    def move(self):
        self.x -=1
        print "初始位置是：",self.x,self.y
class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        # super.__init__()
        self.hungry=True
    def eat(self):
        if self.hungry:
            print("吃吃吃 ")
            self.hungry=False
        else:
            print("吃饱了")
fish=Fish()
fish.move()
fish.move()
shark=Shark()
shark.eat()
shark.eat()

class Base1:
    def fool(self):
        print("base1")
class Base2:
    def foo2(self):
        print("base2")
class C(Base1,Base2):
    pass

c=C()
c.foo2()
c.fool()