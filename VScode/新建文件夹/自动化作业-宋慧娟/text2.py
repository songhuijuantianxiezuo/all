import unittest

from test_case01 import TestStringMethods01
from test_case02 import TestStringMethods02
from test_case03 import TestStringMethods03



test_cases = (TestStringMethods01,TestStringMethods02,TestStringMethods03)


def load_tests(loader, tests):
    suite = unittest.TestSuite()
    for test in tests:
        tes = loader.loadTestsFromTestCase(test)
        suite.addTests(tes)
    return suite

loader = unittest.TestLoader()

suite = load_tests(loader, test_cases)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)
# unittest.runner
