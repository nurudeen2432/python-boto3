import boto3
import os
import logging

from botocore.exceptions import ClientError


def file_upload(file_name,bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)




    client = boto3.client("s3")
    try:
        response = client.upload_file(file_name,bucket, object_name)
        print("upload successful")
    except ClientError as e:
        logging.error(e)
        return False
    return True

file_upload('/home/nuruboy001/python-boto3/create_bucket.py','order-of-store')
