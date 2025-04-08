import os
import boto3
from dotenv import load_dotenv

load_dotenv()

# instantaite client
client=boto3.client('s3')

# set some variables 
bucket='python-aws-s3-prac'
curr_path=os.getcwd()
filePath='opm.jpg'
filename=os.path.join(curr_path + '/uploads', filePath)

# open the file
data=open(filename, 'rb')

# load the data to S3 bucket
client.upload_file(filename, bucket, 'uploaded_image_file')