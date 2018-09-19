import requests
response = requests.get('http://www.baidu.com')
try:
    file = open('shj.html','w',enconding='utf-8')
    file.write(response.text)
except:
    print('error')
finally:
    file.close()
# print(response.text)


