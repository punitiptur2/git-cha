import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

# Launch EC2 instance
response = ec2.run_instances(
<<<<<<< HEAD
    ImageId='ami-Linux',   # Amazon Linux 2 AMI
=======
    ImageId='ami-Linux',   # Amazon Linux 2 AMI
>>>>>>> f8bef306501b2669dc0871028b3adb495939001d
    InstanceType='t3.micro',
    KeyName='my-key-pair',
    MinCount=1,
    MaxCount=1
)

# Print Instance ID
instance_id = response['Instances'][0]['InstanceId']

print("EC2 Instance Created:", instance_id)
