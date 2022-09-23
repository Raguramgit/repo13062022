#AWS Boto3 codes
"""import boto3
iam = boto3.resource('iam')
user = iam.User('RAM')
user = user.create(
    Path='/',
    PermissionsBoundary='arn:aws:iam::aws:policy/AdministratorAccess',
    Tags=[
        {
            'Key': 'Department',
            'Value': 'IT'
        },
    ]
)
import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('ram22092022')
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint':'ap-southeast-1'
    },
    ObjectLockEnabledForBucket=False,
    ObjectOwnership='BucketOwnerPreferred'
)
import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('ram22092022')
response = bucket.delete(
    ExpectedBucketOwner='545965103554'
)
import boto3
s3 = boto3.resource('s3')
s3.Bucket('ram22092022').upload_file('C:\\Users\\63486\\Documents\\PF.jpg','PF.jpg')"""
import boto3
ec2 = boto3.resource('ec2')
instances = ec2.create_instances(
        ImageId="ami-0f62d9254ca98e1aa",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="AWSkey"
    )