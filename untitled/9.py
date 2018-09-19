import os
import re
import shutil
# file=open('9.txt','w')
# os.rename('9.txt','10.txt')
# os.remove('10.txt')
# print(os.getcwd())  #得到现在的路径
# os.chdir('C:')
# print(os.system('terraform init'))  为什么会出乱码？
# os.mkdir('10')
# os.rmdir('10')
# file=open('q','r+',encoding='utf-8')
# file.write('qqqq')
# print(file.read(2))
# os.chdir('C:')
# os.mkdir('hello1')
# file=open('log.txt','a+',encoding='utf-8')
# a=str(os.system(input()))
# file.write(a)
# file.close()
# key=r'<hl>hello world<hl>'
# pl=r'h'
# patternl=re.compile(pl)  #compile
# res=re.findall(patternl,key)
# print(res)
#print(patternl.findall(key))   #findall遍历匹配；search是匹配到一个就结束
# with open('ww','w',encoding='utf-8') as file:
#     file.write('aaaaaaaaa')
# shutil.copyfile('ww','ddd')
# shutil.move('DDD','venv/DDD')
import glob
print(glob.glob('*.py'))


