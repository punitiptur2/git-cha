import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

# Launch EC2 instance
response = ec2.run_instances(
    ImageId='ami-Linux',   # Amazon Linux 2 AMI
    InstanceType='t2.micro',
    KeyName='my-key-pair',
    MinCount=1,
    MaxCount=1
)

# Print Instance ID
instance_id = response['Instances'][0]['InstanceId']

print("EC2 Instance Created:", instance_id)
