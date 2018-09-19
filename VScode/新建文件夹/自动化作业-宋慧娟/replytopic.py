from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://118.31.19.120:3000/signin')

#登录
driver.find_element_by_id('name').send_keys('testuser6')
driver.find_element_by_id('pass').send_keys('123456')
driver.find_element(By.CLASS_NAME,'span-primary').click()
#选择第一条
driver.find_element(By.XPATH,'//*[@id="topic_list"]/div[1]/div/a').click()
#回复
ele=driver.find_element(By.CLASS_NAME,'CodeMirror-code')
ActionChains(driver).move_to_element(ele).click().send_keys('我是回复的内容').perform()
#提交
driver.find_element(By.CLASS_NAME,'span-primary').click()
