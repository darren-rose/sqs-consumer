import os
import boto3

sqs = boto3.resource('sqs')

QUEUE_NAME = os.getenv('QUEUE_NAME')

if QUEUE_NAME is None:
    print('mandatory environment variable QUEUE_NAME does not exit')
    exit(-1)

queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)

while True:
    for message in queue.receive_messages():
        print('{0}'.format(message.body))

