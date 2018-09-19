from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('https://account.aliyun.com/register/register.htm')
frame = driver.find_element_by_css_selector('#alibaba-register-box')
driver.switch_to_frame(frame)
driver.find_element_by_id('nick').send_keys('dddddd')