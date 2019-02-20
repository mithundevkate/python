import boto3

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

'''
client = boto3.client('cur' ,'us-east-1' )
response = client.describe_report_definitions(
    MaxResults=123,
    NextToken='string'
)

print(client)
'''
