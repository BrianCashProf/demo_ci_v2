'''
Simple demo of CircleCI Continuous Integration.
The example here uses the same diction as AWS lambda.
However, it is only an adding method.
'''

# This one adds
def addition(x, y):
    ans = x+y
    return ans
#
def subtraction(x, y):
    ans = x - y
    return ans

def lambda_handler(event, context):
    ans = event['body']
    return ans