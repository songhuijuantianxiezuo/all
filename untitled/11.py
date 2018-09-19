from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# driver.find_element_by_id("kw").send_keys("hellowrld")
# driver.find_element_by_id("kw").clear()
#
# time.sleep(3)
# driver.quit()
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# # driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
# time.sleep(3)
# # driver.find_element_by_partial_link_text('新').click()
# a = driver.find_elements_by_tag_name('a')
# b =[]
# for i in a:
#     name = i.get_attribute('name')
#     print('name:',name,'text',i.text) #i.text把i的文本部分输出
#     b.append(i)

# driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
# time.sleep(1)
# driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('15000011941')
# driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys('324476')
# driver.find_element_by_id('TANGRAM__PSP_10__submit').click()

# driver = webdriver.Chrome()
# driver.get('http://118.31.19.120:3000/')
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[6]/a').click()
# driver.find_element_by_id('name').send_keys('testuser3')
# driver.find_element_by_id('pass').send_keys('123456')
# driver.find_element_by_id('pass').submit()
# driver.find_element_by_xpath('//*[@id="create_topic_btn"]/span').click()
# driver.find_element_by_id('tab-value').click()
# driver.find_element_by_xpath('//*[@id="tab-value"]/option[2]').click()
# driver.find_element_by_id('title').send_keys('1111111')
# a = driver.find_element_by_css_selector('.CodeMirror-scroll')
# ActionChains(driver).move_to_element(a).click().send_keys('sssssssssss').perform()   #perform()

# driver = webdriver.Chrome()
# driver.get('http://118.31.19.120:3000/')

from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('http://www.baidu.com')

driver.find_element_by_link_text('新闻').click()

driver.back()

driver.forward()

driver.refresh()

driver.minimize_window()

driver.close()