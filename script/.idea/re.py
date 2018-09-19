import re
# print(re.match('www', 'www.runoob.com').group())  # 在起始位置匹配   #span()是指匹配的位置
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
# line = "Cats are smarter than dogs"
# matchObj = re.match(r'(.*) are (.*?) .*', line)
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")
# print(re.search('www', 'www.runoob.com').group())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').group())         # 不在起始位置匹配

# pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
# m = re.search(pattern,'one12twothree34four').group()       # 查找头部，没有匹配
# print(m)
# pattern = re.compile(r'\d+')
# m = pattern.search('12312m6666666666666666634four', 1, 10).group() #5,10是指开始匹配的起始位置
# n = pattern.findall('12312m6666666666666666634four',1,100)     #findall不需要group()
# print(m)
# print(n)
# pattern = re.compile(r'\d+')  # 查找数字
# result1 = pattern.findall('runoob 123 google 456')
# result2 = pattern.findall('run88oob123google456', 0, 10)
#
# print(result1)
# print(result2)
# s = '2017-11-27'
# print(re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1', s))
# pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
# m = pattern.match('Hello World word helo').group()
# print (m)
# Python 字典类型转换为 JSON 对象
# import json
# data1 = {
#     'no': 1,
#     'name': 'Runoob',
#     'url': 'http://www.runoob.com'
# }
#
# json_str = json.dumps(data1)
# print("Python 原始数据：", repr(data1))
# print("JSON 对象：", json_str)
#
# # 将 JSON 对象转换为 Python 字典
# data2 = json.loads(json_str)
# print(data2)
# import time
#
# # localtime = time.asctime( time.localtime(time.time()) )
# # print ("本地时间为 :", localtime)
#
# a = time.strftime("%z",time.localtime())   #此处用localtime();%m是指月；%M是指分钟
# print(a)
# import calendar
#
# cal = calendar.month(2018,8)
# print ("以下输出2016年1月份的日历:")
# print (cal)
# def procedure():
#     time.sleep(2.5)

# time.clock
# t0 = time.clock()
# procedure()
# print(t0)
# print (time.clock())

# time.time
# t0 = time.time()
# procedure()
# print(t0)
# print (time.time())
# m = calendar.calendar(2018)
# m = calendar.monthcalendar(2018,8)
# print(m)
# help(time)
# print(dir([]))
# a =list(i for i in range(3,20,2))
# b = a[slice(1,5,2)]     #切片
# print(a)
# print(b)
# a = input("dsdcsd")
# print(type(a))
# import time
# b = input("如果您想看现在的时间，请选a：")          #eval的灵活用法
# a = time.asctime(time.localtime(time.time()))
# c = eval(b)
# print(c)
# fo = open(r"C:\Users\lenovo\Desktop\runoob.txt", "w+")
# fo.write("gggggggggggggggggg\nhhhhhhhhhhhhhh\rjjjjjjj")
# print("文件名为: ", fo.name)
#
# line = fo.read()
# print("读取的数据为: %s" % (line))
#
# # 重新设置文件读取指针到开头
# fo.seek(30, 0)
# line = fo.readline()
# print("读取的数据为: %s" % (line))
#
#
# # 关闭文件
# fo.close()
# print ("round(70.23456) : ", round(70.23456))
# print ("round(56.659,1) : ", round(56.659,1))
# print ("round(80.264, 2) : ", round(80.264, 2))
# print ("round(100.000056, 3) : ", round(100.000056, 3))
# print ("round(-100.000056, 3) : ", round(-100.00056, 3))
# a = "dsfdfsfsfd"
# print(a[1:6:2])
# a = [7,5,3,7,3,2]
# b = set(a)
# print(b)
# str = "this is string example from ruYoob....wow!!!"
#
# print ("str.capitalize() : ", str.capitalize())
# a = "gg"
# b = "hhgghhgghhgg"
# print(b.count(a,1,11))
# f = open(r'C:\Users\lenovo\Desktop\www.csv','r')
# # f.close()
# for j in range(1,5,2):
#     print(f.readline())
# count = 0
# for line in f:
#     if count == 3:
#         print(line)
#     count += 1
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.encoding)
# import os
# # print(os.getcwd())
# os.chdir(r'C:\Users\lenovo\Desktop')
# print(os.getcwd())
# import re
# a = 'dsfdgfdghghfg.fddgdf.gdfgdgdf.fdgdgdfg'
# b = re.compile('.+?\.')
# c = b.search(a).group()
# print(c)
# import requests
# import re
# import urllib.request as uq
# response = requests.get('http://www.ivsky.com/tupian/haiyangshijie/index_2.html')
# fo = open(r'C:\Users\lenovo\Desktop\www.txt','w+',encoding='utf-8')
# fo.write(response.text)
# a = response.text
# # b = '(?<=img src=").+?(?=")'
# # b = 'img src="(.+?/.jpg)"'
# c = re.compile(r'<img src="(http:.+?\.jpg)"')     #如果没有括号，则匹配全部，如果有括号，则匹配括号中的内容
# d = re.findall(c,a)
# fo.close()
# print(d)
# i = 0
# for x in d:
#     uq.urlretrieve(x,r'C:\Users\lenovo\Desktop\新建文件夹\%s.jpg'%i)
#     i += 1
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# print(dict(zip(questions, answers)))
# for a,b in zip(questions, answers):
#     print("aaaaaaa{0}ffffffff{1}".format(a,b))
# with open(r"C:\Users\lenovo\Desktop\www.txt",'a+') as fo:
# # fo = open(r"C:\Users\lenovo\Desktop\www.txt",'a+',encoding='utf-8')
#     fo.seek(0,0)
#     for i in range(0,5):
#         print(fo.readline())
# fo.close()
# f = open(r"C:\Users\lenovo\Desktop\www.csv",'r',encoding='utf-8')
# for i in range(5):
#     print(f.readline())
# import re
#
# line = "Cats are smarter than dogs"
# # a = re.compile(r'(.*?) are (.*)')
# matchObj = re.match(r'(.*?) are (.*)', line)
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.groups())        #注意这里groups()和group()的区别
#     # print("matchObj.group(1) : ", matchObj.group(1))
#     # print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# a = list(enumerate(seasons))
# print(a)
# b = dict(a)
# print(b)
# for i in range(0,4):
#     print(b[i],end=' ')

# x = 10
# expr = """
# z = 30
# sum = x + y + z
# print(sum)
# """
#
#
# def func():
#     y = 20
#     exec(expr)
#     exec(expr, {'x': 1, 'y': 2})
#     exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})       #以字典的方式将数据传入exec()函数中
#
#
# func()


# def is_odd(n):
#     return n % 2 == 1
#
#
# tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])   #过滤掉不符合函数要求的列表数据
# newlist = list(tmplist)
# print(newlist)

# issubclass(B,A)    #判断B是否属于A的子类