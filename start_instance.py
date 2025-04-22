import boto3

from botocore.exceptions import ClientError

import logging

client = boto3.client('ec2')
def start_instances():
    try:
        response= client.start_instances(
            InstanceIds=[
                'i-04e9c685057134ec1'
            ]
        )
        print(response)
        for instance_state in response['StartingInstances']:
            print(f" Your ec2 instance is currently {instance_state['CurrentState']}")
    except ClientError as e:
        logging.error(e)

start_instances()