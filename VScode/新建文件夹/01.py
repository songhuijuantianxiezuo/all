# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Chrome()

# driver.get('http://118.31.19.120:3000/signin')

# driver.find_element_by_id('name').send_keys('testuser1')
# driver.find_element_by_id('pass').send_keys('123456')

# driver.find_element_by_class_name('span-primary').click()

# driver.find_element_by_class_name('span-success').click()

# # 下拉框

# driver.find_element_by_id('tab-value').click()
# driver.find_element_by_css_selector('#tab-value > option:nth-child(2)').click()

# # driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[1]/a[7]').click()
# # time.sleep(5)
# # driver.find_element_by_class_name('webuploader-element-invisible').send_keys(r'C:\Users\lenovo\Desktop\3.jpg')
# # #上传图片找input，然后send_keys输入图片地址
# ele = driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[2]/div[6]')
# #ActionChains(driver).move_to_element(ele).click().send_keys('dsadads').perform()
# ActionChains(driver).move_to_element(ele).click().key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).perform()
# #b必须是小写
# from selenium import webdriver


# driver= webdriver.Chrome()

# driver.implicitly_wait(30)
# # driver.minimize_window()
# # driver.maximize_window()

# driver.get('https://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('helloworld')
# # driver.back()
# # driver.forward()
# # driver.refresh()
# driver.find_element_by_id('su').click()

# driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()

# allwindows = driver.window_handles  #获取的值是数组
# print(len(allwindows))


# l = len(allwindows)
# # driver.set_window_size()

# driver.switch_to_window(allwindows[l-1])

# driver.find_element_by_id('query').clear()
# driver.find_element_by_id('query').send_keys('abcdef')   #submit();quit()
from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(30)

driver.get('http://118.31.19.120:3000/signin')


driver.find_element_by_id('name').send_keys('testuser1')
driver.find_element_by_id('pass').send_keys('123456')


driver.find_element_by_id('pass').submit()

driver.get('http://118.31.19.120:3000/user/testuser1')

driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/a').click()

driver.find_element_by_class_name('fa-trash').click()


alert = driver.switch_to_alert()

text =  alert.dismiss()
print("text",text)

alert.accept()