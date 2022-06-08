'''
Simple demo of CircleCI Continuous Integration.
The example here uses the same diction as AWS lambda.
However, it is only an adding method.
'''


def lambda_handler(event, context):
    ans = event + context
    ans = event + context
    return ans

def lambda_handler2(event, context):
    ans = event - context
    return ans