#coding=UTF-8
from selenium import webdriver
from logging_py import log
import csv 
def getdata():
    with open('./data.csv',encoding='utf-8') as fo:
        # next(fo) #正确
        f = csv.reader(fo)
        next(f)  #正确
        all = []
        for row in f:
            print(row)
            print(" ".join(row))
            all.append(row)
        print(all)
        return all
       
def getdriver()
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    return driver

def register(*list):
    driver = getdriver()
    driver.get('http://118.31.19.120:3000/signup')

    

if __name__=='__main__':
    register()
