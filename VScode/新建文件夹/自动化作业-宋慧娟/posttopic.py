#coding utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest
class test
driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("http://118.31.19.120:3000/signin")
driver.find_element_by_id('name').send_keys("testuser3")
driver.find_element_by_id("pass").send_keys("123456")
driver.find_element_by_id("pass").submit()
driver.maximize_window()
driver.find_element_by_link_text("发布话题").click()
driver.find_element_by_xpath('//*[@id="tab-value"]').click()
driver.find_element_by_xpath('//*[@id="tab-value"]/option[2]').click()
driver.find_element_by_id("title").click()
driver.find_element_by_id("title").send_keys("测试-SHJ")
a = driver.find_element_by_css_selector("#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll")
a.click()
ActionChains(driver).move_to_element(a).key_down(Keys.CONTROL).send_keys("b").key_up(Keys.CONTROL).perform()
b = driver.find_element_by_css_selector("#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > pre > span")
ActionChains(driver).move_to_element(b).click().send_keys("自动化测试").perform()
driver.find_element_by_css_selector('#create_topic_form > fieldset > div > div > div.editor_buttons > input').click()

