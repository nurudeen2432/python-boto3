import boto3

from botocore.exceptions import ClientError

import logging

client = boto3.client('ec2')
def start_instances():
    try:
        response= client.terminate_instances(
            InstanceIds=[
                'i-019ba2788b8657541'
            ]
        )
        #print(response)
        for instance_state in response['TerminatingInstances']:
            print(f" Your ec2 instance is currently {instance_state['CurrentState']}")
    except ClientError as e:
        logging.error(e)

start_instances()