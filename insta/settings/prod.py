from .base import *

DEBUG = False

ALLOWED_HOSTS = ['instagrum-xdvsz.ondigitalocean.app', '10.244.5.105']

# Use S3 as the storage backend for both static and media files
AWS_STORAGE_BACKEND = 's3'
AWS_S3_REGION_NAME = 'sfo3'
AWS_S3_ENDPOINT_URL = 'https://sfo3.digitaloceanspaces.com'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = 'django-instagrum.sfo3.digitaloceanspaces.com'
AWS_STORAGE_BUCKET_NAME = 'django-instagrum'

# Static files settings
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Media files settings (if needed)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
