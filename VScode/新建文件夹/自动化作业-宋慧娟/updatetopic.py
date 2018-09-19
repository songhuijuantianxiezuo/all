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
#点击我的
driver.find_element(By.CLASS_NAME,'user_avatar').click()
#选择第一条
driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[2]/div/a').click()
#点击编辑
driver.find_element(By.XPATH,'//*[@id="manage_topic"]/a[1]/i').click()
#更新内容
ele=driver.find_element(By.CLASS_NAME,'CodeMirror-code')
ActionChains(driver).move_to_element(ele).click().send_keys('我是更新的数据').perform()
#点击提交
driver.find_element(By.CLASS_NAME,'span-primary').click()