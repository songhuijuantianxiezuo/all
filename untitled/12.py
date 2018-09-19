from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import csv
import time
driver = webdriver.Chrome()
# driver.get('https://login.anjuke.com/login/form')
# driver.switch_to.frame('iframeLoginIfm')
# driver.find_element_by_css_selector('#phoneIpt').send_keys('1111')
# driver.switch_to.default_content()
# driver.find_element_by_css_selector('.ajk-icon.user-iconfont').click()
# driver.find_element_by_xpath('/html/body/div[4]/ul/li[3]/a').click()
def login(username,passwd):

    driver.get("http://118.31.19.120:3000/signin")
    time.sleep(3)
    driver.find_element_by_id('name').send_keys(username)
    driver.find_element_by_id('pass').send_keys(passwd)
with open('01.csv') as csvfile:
    a =csv.reader(csvfile)
    next(a)
    for b in a:
        print(b)
        d =','.join(b)
        print(d)
        c = d.split(',')
        print(c)
        login(c[0],c[1])


