import boto3
import os
access_key_id = "AKIATCXMJIOGWMYFHK7W"
secret_key = "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"
client = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_key)

bucket = "datacollector123"
folder = "./DATACOLLECTOR_DATASET/"
for file in os.listdir(folder):
    client.upload_file(folder+file,bucket,file)