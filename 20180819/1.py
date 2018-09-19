#c:\users\lenovo\appdata\local\programs\python
# import math
# from selenium import webdriver
# browser=webdriver.Chrome()
# browser.get('http://www.kugou.com/')
# button1=browser.find_element_by_css_selector('.searh_btn').click()
# checkbox1=browser.find_element_by_css_selector('.search_icon.checkall').click()
# button2=browser.find_element_by_css_selector('.play_all').click()

# if True:
#     print ("Answer")
#     print ("True")
# else:
#     print ("Answer")
#     print ("False") # 缩进不一致，会导致运行错误


# a=input()
# print(a)
#
# b=".....sssssssssssssssss.........."
# print(b.strip('.'))
#
# print(a+b)

# e="shdjjncjkxcmckdd"
# f=e.find(".")
# print(f)
#
# # g=e.index('.')
# # print(f)
#
# print("a"not in e)
# print(help(e.strip))

# from selenium import webdriver
# print(help(webdriver))

# import math
# print(help(math))

# import pandas as pd
# print(help(pd))


# num=35687
# if num>=0 and num<=100:
#     if num>=80 and num<=100:
#         print('good')
#     if num>=60 and num<80:
#         print('just so so')
#     if num >=0 and num<60:
#         print('bad')
# else:
#     print('error')

# list=[1,2,3,'ee',5]
# list.pop()
# print(list)
# a='dsadsadasdadas'
# print(a[0])
# list.append(a)
# print(list)
# list1=[1,2,3,]
# # list1.extend(list)
# list=list+list1
# print(list)
# a=('a','s')
# b=('s','f')
# c=a+b
# print(type(b))

# a=(1,2,3,[1,2,3])
# # b=(1,2,3,[2,2,3])
# for i in a:
#     if type(i)==class 'list':
#        i[0]=2
# print(a)

# b[3][0]=3
# print(b)
# a='dfdsfdsfds'
# for i in a:
#     i='1'
# print(i)
# list7=['a','s','d','g','f','h']
# i=input()
# # for a in list7:
# #     if i==a:
# #         print('该元素属于列表中')
# #
# # print('该元素不属于列表中')
# if i not in list7:
#     print('T')
# else:
#     print('F')

# a='dsadeadsa'
# i=input()
# if i in a:
#     print(i)
# if
# elif



# for i in range(1,10):
#     for j in range(1,10):
#         if j<=i:
#             print(i,' ',j,' ',i*j,end='\t')         #\t空格,杠t是反斜杠
#     print(' ')

# import math
# i=int(input())
# for i in range(1,11):
#     if i==5:
#         print(i)
#         break

# a=int(input())
# i=0
# while i<11:
#     if a==5:
#         print('此时输入的数字是5')
#         break  # break跳出第一个循环
#     i+=1

# for i in range(0,9):
#     print('i=',i)
#     for j in range(0,5):
#         print('j=',j)
#         if j==5:
#             break
#


# for i in range(0,9):
#     print('第一次',i)
#     if i==5:
#          continue
#     print('第二次', i)
# continue 继续最内层循环；break跳出最内层循环；pass就是什么也不做，主要是为了防止语法错误

# import math
# math.sqrt()
# x=1
# while x>0:
#     if math.sqrt(x+168)-math.sqrt(x+100)==int()
#           print(x)
#           x+=1
#           break

# print(math.sqrt(10))
# append是指加列表中一个元素，extend是将两个列表连起来
# clear 清除列表中的元素；del 清除列表；copy复制列表；index取下标，传一个值，看这个值在列表中第一次出现的位置
# a=[1,2,3,4,5,6,2,3,4]
# b=[]
# for i in a:
#     if i in b:
#         continue
#     else:
#         b.append(i)
#         print()
# set去除列表中的重复值
# a='safdsfsa'
# print(set(a))
# b=list(reversed(a))
# print(b)
# a.remove(2)
# b=list(a)
# b.reverse()
# a=str(b)
# print(b)
# remove只能删除列表中的元素，不能删除字符串中的单个字符
# reverse只能颠倒列表中的元素，不能颠倒字符串中的字符
# sorted排序
# a=[1,2,3,4,5,6,2,3,4]
# # print(sorted(a)) #临时性排序
# # a.sort()   #永久性排序
# a.insert(20,2)
# a.append(9)
# a=a*3   #列表的乘法是列表重复出现了3次
# print(a,len(a))  #len是测列表中元素的个数

# xiaoming={1:'ddd',2:'sdsad',3:'sssssssssss'}
# print(xiaoming['a'])
# print(xiaoming.keys())
# print(xiaoming.values())
# print(xiaoming.items())  #单个组放在元组里，全部组放在列表里
# # xiaoming.clear()
# # print(xiaoming)
# # a=list(xiaoming.fromkeys([1,2,3],[4,5,6])
# # print(a)
# # xiaoming.popitem()  #随即删除，不一定是删最后一个
# print(xiaoming)
# del xiaoming
# xiaoming={1:'ddd',2:'sdsad',3:'sssssssssss'}
# xiaoming[2]='ssss'
# xiaoming[4]='dddddddddd'
# print(xiaoming)
# print(len(xiaoming))
# xiaoming.popitem()
# a=str(xiaoming)
# print(a)
# 如果键重复，则后出现的值会替代前面的值，不会报错。键必须是不可变的
# i=1
# j=1
# while i<2000:
#     while j<2000:
#         i,j=j,j+i  #将j赋值给i,将j+i赋值给j      i,j=j,i  #交换i和j的值
#         print(i)


# import json    drumps转化成JSON格式   loads由JSON格式转出
# list1=[1,2,3,4,5,6,7,8,9]
# print(list1[1:-1:2])   #-1则取不到最后一个
# list2=['w','e']
# list1.append(list2)
# list1.extend(list2)
# print(list1.count())
# list1.sort()
# list1.remove(2)
# list1.pop(1)
# list1.reverse()
# list.clear()
# print(list1)
# tuple1=('w',)
# type(tuple1)
# tuple1.index()
# list(tuple1)
# tuple(list1)
# dict1={1:2,3:4,5:6}
# dict1.popitem()
# del dict1[1]
# dict1.pop(2)
# dict1.keys()
# dict1.values()
# dict1.items()
# dict[3]
# dict1.get(3)
# dict1[3]=999
# dict[4]=223
# dict1.fromkeys([1,2,3],'hi')
# dict1.clear()
# dict1.copy()
# #dict是无序的，list是有序的   其它方面，dict的用法类似list
#set是去重
# a=[1,1,1,2,3,4]
# b=list(set(a))
# print(b)
#


























