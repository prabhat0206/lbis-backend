import boto3
from botocore.config import Config
from os import environ
from dotenv import load_dotenv
import string, random

load_dotenv()

s3 = boto3.client(
   "s3",
   config=Config(signature_version='s3v4'),
   aws_access_key_id=environ.get('S3_KEY'),
   aws_secret_access_key=environ.get('S3_SECRET'),
   region_name=environ.get('S3_REGION')
)

def upload_file_to_s3(file):
    better_filename = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 18))
    s3.upload_fileobj(
        file,
        environ.get('S3_BUCKET'),
        better_filename,
        ExtraArgs={
            "ACL": "public-read",
            "ContentType": file.content_type
        }
    )
    return f"https://{environ.get('S3_BUCKET')}.s3.amazonaws.com/{better_filename}"


