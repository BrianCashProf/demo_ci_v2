'''
This is the test for the lambda_handler.
It utilizes unittest.
'''

import unittest
import demo


class MyTestCase(unittest.TestCase):
    def test_adding(self):
        ans = demo.lambda_handler(1,1)
        self.assertEqual(2, ans)  # add assertion here

    def test_subtracting(self):
        ans = demo.lambda_handler2(1,1)
        self.assertEqual(2, ans)  # add assertion here


if __name__ == '__main__':
    unittest.main()
