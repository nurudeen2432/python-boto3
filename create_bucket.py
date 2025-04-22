import boto3
import os
import logging

from botocore.exceptions import ClientError

#we invoke the boto3 client or aws client
client = boto3.client("s3")

#request method where we call the client
response=client.create_bucket(
Bucket='order-of-store',
CreateBucketConfiguration={
    'LocationConstraint':'us-west-1'
}
)
print(f"bucket created {response}")

















