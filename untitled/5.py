import math
# a='a'
# b=[1,2,3,4]
# c=(1,2,3,)
# d={1:2,3:4,5:6}
# e=input()
# f='.....aaaaaabnnnnnaaaaaa......'
# f=f.strip('.')
# print(f)
# s=f.find('a')
# print(f.find('c'))  #查找不到-1,find和index后面都是跟值，返回角标
# f.index('a')
# print(f.index('c'))   #差找不到则报错
# n=input()
# n=int(n)
# while n>1:
#     if n<10:
#         print('1')
#         n-=2
#     else:
#         print('2')
#         break
#while循环，往复执行，break跳出循环
# m='12345678'
# for i in m:
#     print(i,end='\t')
# print(type(len(m)))
# for i in range(0,len(m),2):
#     print(i)
#help(type)  #直接用help也可以，不一定要打印才能出来
# a=[1,2,3,4,5,6]
# a.remove(2) #remove后面跟所要删除的值
# a.pop(4)  #pop后面跟所要删除的角标
# del a[3]   #del也可以用于删除列表中的元素，只要列表后面加角标
# # a.clear()
# del a
# print(a)
# a=[1,2,3,4,5,6,7,9,8]
# # a.sort()  #永久性排序
# b=sorted(a)    #临时性排序
# # a.reverse()   #永久性颠倒
# # b=reversed(a)   #颠倒的数列所在的位置
# a.append(10)
# a.extend(b)
# print(a)
# c=a.count(10)   #count()里面填列表的值，数字不加引号，字符串加引号，表示该值在该列表中的计数
# print(c)
# a=(5,)
# print(type(a))
# a={1:2,3:4,5:6}
# a.popitem()   #pop括号中必填键，否者报错     popitem()后必不能加角标，否则报错，因字典是无序的，故popitem删除是随机删除
# print(a.keys())   #keys后面必加括号，否则报错
# print(a.values())
# print(type(a.items()))
# b=dict.fromkeys([1,2,3],[1,2,3])
# print(b)
# a=(1,2,3,4)
# del a[0]
# print(a)
# y=lambda x:x+1
# a='dewdewde'
# del a[2]
# print(a[2])   #字符串不支持删除其中某个词
# a=(1,2,[1,2,3])
# a[2].remove(2)
# print(a)   #元组中的列表可以改变，因为元组实际存储的是元素列表的地址；但元组中的字符串不可以改变
e=[1,2,3,4,5,6,7,7,7,7]   #最后一个是-1，往前依次-2，-3...
# # print(a[-5:-2])    #相当于倒叙切割
# # b=set(a)     #去重
# # print(type(b))  #b的种类是set
# # c=list(b)   #强转为列表类型
# # print(c)
# # b=a.reverse()   #reverse相当于一个函数，返回值无，功能就是倒叙
# a.insert(2,1)    #在a的第2位上插入1
# print(a)  #这个不对，输出的是a的倒叙的储存地址
# b=[i for i in a]  #列表生成式
# c=[i for i in range(0,10,2)]
# print(c)
# def a(b):
#     c=b*2
#     return c
# print(a(e))
# def a(q,*s):    #*代表不定长参数
#     c=q*s
#     return c
# print(a(3,[2,3]))    #输出的结果是元组([2, 3], [2, 3], [2, 3])
# a=lambda x,y:x+y+1
# print(a(1,2.2))
b=1
# def a():
#     print(b)
# def c(d):
#     print(d)
#     global b     #不能写成global b=3，否则报错
#     b=3
#     a()
# c(2)
# def a(e):
#     print(e)
#     def c(d):
#         print(d)
#         nonlocal e     #不能写成global b=3，否则报错
#         e=3
#         a(e)
#     c(1)
# a(2)
# i=3
# def c():
#     i=4
#     def a():
#         i=1
#         def b():
#             nonlocal i
#             #global i     #global所变更的是全局变量，最外层的变量；nonlocal所变更的是局部变量，只变更倒数第二层的变量
#             i=2
#             print(i)
#         b()
#         print(i)
#     a()
#     print(i)
# c()
# print(i)
# for a in range(-1,7):
#    if a==1:
#        continue    #循环中continue后面的语句执行不到
#        print(1)
#    elif a==2:
#        print(2)
#        break
#    else:
#        pass
# continue 继续最内层循环；break跳出最内层循环；pass就是什么也不做，主要是为了防止语法错误
# import json
# a=(1,2,3,4)
# b=json.dumps(a)   #dumps编码（转化为JSON格式）；loads解码（转化为PYTHON格式）
# print(b,type(b))
# c=json.loads(b)
# print(c,type(c))   #元组转化成JSON格式后，再转回来，会变成列表的形式
# a=1
# b=2
# c=3
# d=4
# a,b,c,d=b,a+d,d,c+d  #同时多变量赋值
# print(a)
# print(b)
# print(c)
# print(d)