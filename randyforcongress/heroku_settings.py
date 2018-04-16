import logging
import os

################
# AWS SETTINGS #
################

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_SECRET_KEY_ID']
AWS_S3_REGION_NAME = 'us-east-1'
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = 'randyforcongress'

# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

###################
# DJANGO SETTINGS #
###################

ALLOWED_HOSTS = ["randyforcongress.herokuapp.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ['DATABASE_NAME'],
        "USER": os.environ['DATABASE_USER'],
        "PASSWORD": os.environ['DATABASE_PASSWORD'],
        "HOST": os.environ['DATABASE_HOST'],
        "PORT": "5432",
    }
}

DEBUG = True

NEVERCACHE_KEY = os.environ['NEVERCACHE_KEY']
SECRET_KEY = os.environ['SECRET_KEY']

logging.error(os.environ['SECRET_KEY'])
logging.error(SECRET_KEY)

# Tell the staticfiles app to use S3Boto3 storage when writing the collected
# static files (when you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
