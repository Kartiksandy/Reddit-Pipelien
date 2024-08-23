import s3fs
import boto3
import logging
from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY, AWS_BUCKET_NAME

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key=AWS_ACCESS_KEY_ID,
                               secret=AWS_ACCESS_KEY)
        return s3
    except Exception as e:
        logging.error(f"Failed to connect to S3: {e}")
        raise

def create_bucket_if_not_exist(s3, bucket):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            logging.info("Bucket created")
        else:
            logging.info("Bucket already exists")
    except Exception as e:
        logging.error(f"Failed to create bucket: {e}")
        raise

def upload_to_s3(file_path, bucket_name, s3_file_name):
    s3_client = boto3.client('s3',
                             aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_ACCESS_KEY)
    try:
        s3_client.upload_file(file_path, bucket_name, s3_file_name)
        logging.info(f"File {file_path} uploaded to {bucket_name}/{s3_file_name}")
    except boto3.exceptions.S3UploadFailedError as e:
        logging.error(f"Failed to upload {file_path} to {bucket_name}/{s3_file_name}: {e}")
        raise
