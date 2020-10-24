import boto3

client = boto3.client('rekognition')


s3 = boto3.client('s3')

response = s3.list_buckets()

awsBucket=#AWS Bucket Name
file=#filepath on local machine
awsKeyImg=#Image Name


# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


# Upload a new file
data = open(file, 'rb')
s3.put_object(Bucket=awsBucket,Key=awsKeyImg, Body=data)


#recognizeCelebrity
response = client.recognize_celebrities(
    Image={
        #'Bytes': b'bytes',
        'S3Object': {
            'Bucket': awsBucket,
            'Name': awsKeyImg,
            'Version': #Image version if enabled, add ' '
        }
    }
)

print (response)