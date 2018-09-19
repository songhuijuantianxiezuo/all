import requests
import re
import urllib.request
import os
import os
# response = requests.get('http://jt.sh.cn:8082/wsbs/web/lnfltime/1.jhtml')
# try:
#     file = open('shj1.txt','w',encoding='utf-8')
#     file.write(response.text)
#     # fileread=response.text
#     file.close()    #不能同时读写
#     file1 = open('shj1.txt','r+',encoding='utf-8')
#     fileread=file1.read()
#     key = re.compile(r'<td bgcolor="#fdeae9"  height="26" rowspan="3" width="100">\n\n\t\t\t\t\t\t\t\t\t\t(.*?)\n\n\t\t\t\t\t\t\t\t\t</td>', re.S)
#     res = re.findall(key, fileread)
#     print(res)
# except:
#     print('error')
# finally:
#     file.close()
# print(response.text)
response = requests.get('http://www.ivsky.com/tupian/haiyangshijie/index_2.html')
# try:
file = open('shj2.txt','w',encoding='utf-8')
file.write(response.text)
    # fileread=response.text
file.close()    #不能同时读写
file1 = open('shj2.txt','r+',encoding='utf-8')
fileread=file1.read()
key = re.compile(r'<img src="(.*?)" alt=.+?></a></div>', re.S)
key2 =re.compile(r'http://img.ivsky.com/img/tupian/li/.+?/.+?/(.+?).jpg',re.S)
res = re.findall(key, fileread)
res2= re.findall(key2,fileread)
print(res)
print(res2)
# os.mkdir(r'C:\\Users\\lenovo\\Desktop\\b')
x = 0
# # urllib.request.urlretrieve('http://img.ivsky.com/img/tupian/li/201701/01/haiyang_yuqun-010.jpg' , 'C:\%s.jpg' % x)
for i in res:
     urllib.request.urlretrieve(i, 'C:\\Users\\lenovo\\Desktop\\b\\%s.jpg' % res2[x])
     x+=1
#      # os.rename(res[i],res2[i])
# # except:
# #     print('error')
# # finally:
file.close()

