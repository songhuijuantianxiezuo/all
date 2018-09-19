import unittest


class TestStringMethods02(unittest.TestCase):
# 0-9 A-Z a-z
    @classmethod
    def setUpClass(cls):
        print("befor all case ....")

    def setUp(self):
        print("before every test case exec ......")

    def tearDown(self):
        print('after every test case exec ......')

    def testa_upper(self):
        print("testaaaa")
        self.assertEqual('foo'.upper(), 'FOO',"不相等")

    def testA_isupper(self):
        self.assertTrue('FO8O'.isupper())
        self.assertFalse('Foo'.isupper())

    @unittest.skip('ddd')   #必须要有('')，否则不会被跳过，内容是注释，不会显示
    def test1_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    @classmethod
    def tearDownClass(cls):
        print("after all testcase....")

if __name__ == '__main__':
    unittest.main()