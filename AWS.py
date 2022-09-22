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
)"""
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