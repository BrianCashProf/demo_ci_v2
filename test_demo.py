'''
This is the test for the lambda_handler.
It utilizes unittest.
'''
# Dependencies
import unittest
import json
import os

#scripts
import demo


class MyTestCase(unittest.TestCase):
    def test_adding(self):
        ans = demo.addition(1,1)
        self.assertEqual(2, ans)  # add assertion here

    def test_subtracting(self):
        ans = demo.subtraction(1,1)
        self.assertEqual(0, ans)  # add assertion here

    def test_lambda(self):
        current_directory = os.getcwd()
        demo_dir = os.path.join("json_demo","demo1.json")
        f = open(demo_dir)
        test = json.load(f)
        f.close()
        ans = demo.lambda_handler(test,None)
        ex_ans= {
                "answer 2": "This is the body"
            }
        self.assertEqual(ex_ans, ans)  # add assertion here

if __name__ == '__main__':
    unittest.main()
