import boto3

from botocore.exceptions import ClientError

import logging




def delete_buck():

    client = boto3.client('s3')
    try:
        response = client.delete_bucket(
            Bucket='ibtbuckets3',
            ExpectedBucketOwner='269862533655'
        )
        print(f"bucket {response} deleted !!")
    except ClientError as e:
        #logging.error(e)
        print(f'An Error occurred :- {e}')


delete_buck()