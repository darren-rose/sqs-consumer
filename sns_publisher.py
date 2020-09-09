import os
import boto3

sns = boto3.client('sns')

ACCOUNT_NO = os.getenv('ACCOUNT_NO')
TOPIC_NAME = os.getenv('TOPIC_NAME')

if TOPIC_NAME is None:
    print('mandatory environment variable TOPIC_NAME does not exit')
    exit(-1)

if ACCOUNT_NO is None:
    print('mandatory environment variable ACCOUNT_NO does not exit')
    exit(-2)

response = sns.publish(
    TopicArn='arn:aws:sns:eu-central-1:{0}:{1}'.format(ACCOUNT_NO, TOPIC_NAME),    
    Message='Hello World!',    
)

print(response)

