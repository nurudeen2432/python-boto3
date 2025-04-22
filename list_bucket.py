import logging

import boto3
from botocore.exceptions import ClientError


def list_bucket():
    client = boto3.client('s3')

    try:
        response = client.list_buckets(
            MaxBuckets=10
        )
        for bucket in response['Buckets']:
            print(f"Buckets: {bucket['BucketRegion']}")
        print(response)



    except ClientError as e:
        logging.error(e)

list_bucket()