
import sys
sys.path.append('/Users/zack/Desktop/testdemo')

import unittest
from common.get_driver import get_driver
from po.Baidu import BaiduPage
import time

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=get_driver()

    def test_1(self):

        baidu = BaiduPage(self.driver)
        baidu.open_url("http://www.baidu.com")
        baidu.input_text('a')
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
 


if __name__ == '__main__':
    unittest.main()