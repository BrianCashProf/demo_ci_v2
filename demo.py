'''
Simple demo of CircleCI Continuous Integration.
The example here uses the same diction as AWS lambda.
However, it is only an adding method.
'''

def lambda_handler(event, context):
    return event + context