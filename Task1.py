#import library
from logging import exception
import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Service key Google Cloud.json'

storage_client = storage.Client()

#Create a new bucket

bucket_name = 'kiki_data_bucket'
bucket = storage_client.bucket(bucket_name)
bucket.location = ('US')
bucket = storage_client.create_bucket(bucket)


#Print Bucket Detail

vars(bucket)


#Accessing a Spesifik Bucket

my_bucket = storage_client.get_bucket('kiki_data_bucket')


#upload files

def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

file_path = r'/Users/rifqimanufi/Documents/Visual Studio Code/Python with GCP/data'
upload_to_bucket('order_tab', os.path.join(file_path, 'order_tab.csv'), 'kiki_data_bucket')