from selenium import webdriver
from selenium.webdriver.common.by import By

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
#点击删除
driver.find_element(By.CLASS_NAME,'fa-trash').click()

#弹出窗口点击确认
driver.switch_to_alert().accept()





