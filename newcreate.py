import boto3

s3 = boto3.client("s3")

bucket_name="portfolio-web"

try:

	response =  s3.list_objects_v2(Bucket=bucket_name)
	if 'Contents' in response:
		for obj in response['Contents']:
			s3.delete_object(Bucket=bucket_name, key=obj['key'])
		print("All object deleted")
	s3.delete_bucket(Bucket=bucket_name)
	print(f"s3 bucket {bucket_name} deleted successfully")

except Exception as e :
	print(f"Error deleting {bucket_name}: {e} ")
