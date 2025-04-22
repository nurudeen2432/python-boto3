import logging

import boto3
from botocore.exceptions import ClientError

client = boto3.client('ec2')

def create_ec2():
    try:
        response = client.run_instances(
            BlockDeviceMappings=[
                {
                    'DeviceName':'/dev/ssh',
                    'Ebs':{
                        'VolumeSize':100
                    }

                }
            ],
            ImageId='ami-abc12345',
            InstanceType='t2.micro',
            MaxCount=1,
            MinCount=1
        )
        print(f'{response} displayed')
    except ClientError as e:
        logging.error(e)


create_ec2()