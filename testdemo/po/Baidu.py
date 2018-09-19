import sys
sys.path.append('/Users/zack/Desktop/testdemo')


from common.get_driver import get_driver


from selenium.webdriver.common.by import By
search_input_id="kw"
search_btn=""

class BaiduPage():
    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        self.driver.get(url)

    # 输入文本
    def input_text(self, search_text):
        self.driver.find_element(By.ID,search_input_id).send_keys(search_text)
    

    # 点击搜索框
    def click_search(self, parameter_list):
        pass
    
    # 截屏
    def tack_screenshot_myslf(self,filepath):
        pass

    
    # 保存源码
    def save_source(self, filepath):
        pass



if __name__ == '__main__':
    driver = get_driver()
    baidu = BaiduPage(driver)
    baidu.open_url("http://www.baidu.com")
    baidu.input_text('a')

    

