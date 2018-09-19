# from string import maketrans
# s='fdsFsd'
# s=s.capitalize()
# print(s)
# a = s.center(20,'e')
# print(a)
# sd=['jgh','fhj']
# sd1=[1,2]
# print("ssss{0[0]}+{1[0]}".format(sd,sd1))
# str = "this is string example....wow!!!"
# intab = "aeiou"
# outtab = "12345"
# print(str.maketrans(intab,outtab))
# str = "www.runoob.com.ddd"
# print(str.rfind("."))
# str = "this is strIng example....wow!!!"
# print(str.swapcase())
# str = "this IS string example....wow!!!";
# print(str.upper())
# a = [11, 22, 33]
# a.extend('55')
# #
# a=[0,1,2,3,4,5]
# b=a
# c=a.copy()
#
# del b[1]
# print(a)
# print(b)
# print(c)
# a='joklllmkllkl'
# print(a[1:6:2])
# t=(1,2,3)
# r=(4,5)
# t=t+r
# print(t)
# s={1:2,3:3}
# a = s.fromkeys([1,2,3], [1, 3])
# d=a
# print(a)
# c=s.copy()
# c[1]=4
# print(c)
# print(a)
# print(d)
# print(s)
# dict = {'Name': 'Runoob', 'Age': 7}
#
# print (dict.items())
# dict = {'Name': 'Runoob', 'Age': 7}
# # for i,j in dict.items():
# #     print(i, ":", j)
# dict.items()
# a=list(dict.items())
# print(a)
# dict = {'Name': 'Runoob', 'Age': 7}
# dict1 = {'me': 'Runoob', 'ge': 7}
# print ("Age 键的值为 : %s" %  dict.setdefault('Age', None))
# print ("Sex 键的值为 : %s" %  dict.setdefault('Sex', None))
# print ("新字典为：", dict)
# site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# pop_obj=site.popitem()
# print(site.get('name'))
# print('name  rate'.ljust(20,'-'))
# a = set('abracadabra')
# print(type(a))
# thisset = set(("Google", "Runoob", "Taobao"))
# thisset.add(1)
# print(set([9,4,5,2,6,7,1,8]))
# var1 = -10000000
# if var1:
#     print ("1 - if 表达式条件为 true")
#     print (var1)
# while True:
#     try:
#         age = int(input("请输入您家狗的年龄:"))
#         print(" ")
#         age = float(age)
#         if age < 0:
#             print("您在逗我？")
#         elif age == 1:
#             print("相当于人类14岁")
#             break
#         elif age == 2:
#             print("相当于人类22岁")
#             break
#         else:
#             human = 22 + (age - 2)*5
#             print("相当于人类：",human)
#             break
#     except ValueError:
#         print("输入不合法，请输入有效年龄")
# for i in range(-10, -10000, -30) :
#     print(i)
# while True:
#     number = input('请输入一个整数(输入Q退出程序)：')
#     if number in ['q','Q']:
#         break                #如果输入的是q或Q,结束退出
#     elif not number.isdigit():
#         print('您的输入有误！只能输入整数(输入Q退出程序)！请重新输入')
#         continue         #如果输入的数字不是十进制,结束循环,重新开始
#     else :
#             number = int(number)
#             print('十进制 --> 十六进制 ：%d -> 0x%x' %(number,number))
#             print('十进制 -->   八进制 ：%d -> 0o%o' %(number,number))
#             print('十进制 -->   二进制 ：%d ->'%number,bin(number))
# def printinfo(arg1, **vardict):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vardict)
#
#
# # 调用printinfo 函数
# printinfo(1, a=2, b=6)
# a = 10
#
#
# def sum(n):
#     global  a
#     a = 11
#     n += a
#     print('a = ', a, end=' , ')
#     print('n = ', n)
#
#
# sum(3)
# def fun(a,b):
#     "返回多个值，结果以元组形式表示"
#     return a,b,a+b
# print(fun(1,2))
# print(fun.__doc__)
# def a_function_requiring_decoration():
#     """Hey you! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell")
#
#
# a_function_requiring_decoration()
# a=list(range(1,20))
# i=list([x,x*2] for x in a)
# print(a)
# print(i)
# a='fgffhgfhfg'
# d=eval(a)
# print(d)
# b=list(set(a))
# c=list(a)
# print(a)
# a=list(range(-100,-10,4))
# print(a)
# a=[1,2,3,5]
# b=[3,6,7,8]
# for x,y in zip(a,b):
#     print("--{0}++++{1}".format(x,y))
#     print("------%s__________%s"%(x,y))
# a={1:2,4:3,9:0}
# a.pop(4)
# a.popitem()
# # print(a)
# a=(1,2)
# b=(3,4)
# a=a+b
# # print(a)
# a=[1,2,3]
# # a.pop(1)
# # print(a)
# c=a.index(3)
# print(c)
# a=(1,2,3,4)
# b=a[1::2]
# print(b)
# b=[[x,x*2] for x in a ]
# print(b)
#!/usr/bin/python3

# 打开一个文件


# 打开一个文件
# f = open("C:\\Users\\lenovo\\Desktop\\www.txt", "r+")
#
# f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# # f.seek(21,0)
# # f.write('ffff')
# k=f.read(10)
# print(k)
# # 关闭打开的文件
# f.close()
# f = open("C:\\Users\\lenovo\\Desktop\\www.txt", "a+")
# f.write("a\t")
# print(f.tell())  #此时指针在文件字符末尾处
#!/usr/bin/python3
#
# import os, sys
#
# path = r"C:\Users\lenovo\Desktop"
#
# # 查看当前工作目录
# retval = os.getcwd()
# print ("当前工作目录为 %s" % retval)
#
# # 修改当前工作目录
# os.chdir(path)
#
# # 查看修改后的工作目录
# retval = os.getcwd()
#
# print ("目录修改成功 %s" % retval)
#!/usr/bin/python3
#
# import os, sys, stat
#
# # 假定 /tmp/foo.txt 文件存在，设置文件可以通过用户组执行
#
# os.chmod(r"C:\Users\lenovo\Desktop", stat.S_IXGRP)
#
# # 设置文件可以被其他用户写入
# os.chmod(r"C:\Users\lenovo\Desktop", stat.S_IWOTH)
#
# # print ("修改成功!!")
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('896312051@qq.com', 'jcaesar@example.org',
# """To: jcaesar@example.org
# ... From: soothsayer@example.org
# ...
# ... Beware the Ides of March.
# ... """)
# server.quit()
a=[1,2,3,4,5,6,7,7,7,7]
b = a.reverse()
a.insert(2,1)
print(a)