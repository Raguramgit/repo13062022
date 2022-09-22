#AWS Boto3 codes
import boto3
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