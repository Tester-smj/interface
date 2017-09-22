#coding=utf-8
lis=[11,21,13,4,5,0,8,12]
def bubble_sort(lis):
    count =len(lis)
    print count
    for i in range(0,count):
        for j in range(i+1,count):
            if lis[i]>lis[j]:
                lis[i],lis[j]=lis[j],lis[i]
    return lis

print bubble_sort(lis)