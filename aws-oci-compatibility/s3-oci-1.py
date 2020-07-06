import boto3
import oci

config = oci.config.from_file("~/.oci/config")
s3 = boto3.resource(
    's3',
    aws_access_key_id="23c31d7e0acd7b3b8a7c8d6612ccae4f1257b8d2",
    aws_secret_access_key="4GvmLFkShOQBj/55/ELnNcoHEbvaXnZjBQhShJ4MrxQ=",
    region_identifier="us-phoenix-1",  # Region name here that matches the endpoint
    endpoint_url="https://ateamsaas.compat.objectstorage.us-ashburn-1.oraclecloud.com"  # Include your namespace in URL
)

or

s3 = boto3.resource(
    's3',
    aws_access_key_id=config['aws_access_key'],
    aws_secret_access_key=config['aws_secret_key'],
    region_identifier=config['region'],  # Region name here that matches the endpoint
    endpoint_url="https://ateamsaas.compat.objectstorage.us-ashburn-1.oraclecloud.com"  # Include your namespace in URL
)

####################### List out available buckets ####################################

for bucket in s3.buckets.all():
    print(bucket.name)

##############   create S3 bucket /bject storage ##########################
s3.create_bucket(Bucket=Name
of
the
bucket / object
storage)
response = s3.list_buckets()
print(response)

###################### upload file #######################################
with open(Name of the file, 'r') as f:
    content = f.read()

print(content)

s3.upload_file(Name
of
the
file)


########################### access file from s3 ##########################
s3_resource = boto3.resource('s3')

s3_object = s3_resource.Object(bucket_name=Name
of
the
bucket, key = File
Name or Path in Buket)

from io import StringIO

s3_data = StringIO(s3_object.get()['Body'].read().decode('utf-8'))

data = pandas.read_csv(s3_data)
print(data.head())

######################## Delete bucket / object storage #####################

s3.delete_bucket(Bucket=Name
of
the
bucket / object
storage)
