from logging import exception

import boto3

from botocore.exceptions import ClientError

import logging




def delete_obj():
    client = boto3.client("s3")

    try:
        response = client.delete_object(
            Bucket='order-of-store',
            Delete = {
                'Objects' :[
                    {
                        'Key':''

                    },
                    {
                        'Key': ''

                    }

                ]
            }
        )
        print(response)
    except ClientError as e:
        logging.error(e)

delete_obj()


