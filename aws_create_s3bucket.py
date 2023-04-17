#pip install boto3
#pip install awscli
#configure awscli

import boto3

aws_resource=boto3.resource("s3")

bucket=aws_resource.Bucket("practice_bucketzx34")

response = bucket.create(
    ACL='public-read',
    Bucket='string',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
   
)


print(response)
