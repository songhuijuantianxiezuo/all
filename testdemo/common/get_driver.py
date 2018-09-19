import sys
sys.path.append('/Users/zack/Desktop/testdemo')

from selenium import webdriver


def get_driver():
    driver = webdriver.Chrome()
    return driver