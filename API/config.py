from os import environ
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = 'sqlite:///../sql.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = environ.get('SECRET_KEY')
MAIL_SERVER=environ.get('MAIL_SERVER')
MAIL_PORT=environ.get('MAIL_PORT')
MAIL_USERNAME=environ.get('MAIL_USERNAME')
MAIL_PASSWORD=environ.get('MAIL_PASSWORD')
MAIL_USE_TLS=environ.get('MAIL_USE_TLS')
ADMIN_EMAIL = environ.get('ADMIN_EMAIL')
ADMIN_PASSWORD = environ.get('ADMIN_PASSWORD')
# MAIL_USE_SSL=environ.get('MAIL_USE_SSL')
# S3_SECRET_KEY = environ.get('S3_SECRET_KEY')
# S3_ACCESS_KEY = environ.get('S3_ACCESS_KEY')
# S3_REGION = environ.get('S3_REGION')
# S3_BUCKET = environ.get('S3_BUCKET')
# S3_BUCKET_URL = 'https://{}.s3.amazonaws.com/'.format(S3_BUCKET)