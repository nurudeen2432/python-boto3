import boto3

client =  boto3.client('ec2')


response = client.stop_instances(
	InstanceIds=[
		'i-04e9c685057134ec1'
]

)

for instance_state in response['StoppingInstances']:
	print(f"The current state of {instance_state['InstanceId']} is {instance_state['CurrentState']}")
