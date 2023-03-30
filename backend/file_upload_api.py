from fastapi import FastAPI, File, UploadFile
import boto3
import botocore
import os
import time
import db_helper

app = FastAPI()

# Define your S3 credentials

aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
s3_bucket = os.environ.get('S3_BUCKET')
region_name = os.environ.get('S3_REGION')

# Create a new S3 client
# s3 = boto3.client('s3', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

s3 = boto3.client(
    's3',
    aws_access_key_id="AKIAZW4EPXNK5AQIEQWO",
    aws_secret_access_key="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",
)

s3_bucket = "goes-team6"

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    """
    Uploads a file to an S3 bucket.
    """
    try:
        # Create a key for the file in the S3 bucket
        timestamp = int(time.time())
        key = f"{timestamp}.mp3"
        # Upload the file to S3
        s3.upload_fileobj(file.file, s3_bucket, f"uploads/{key}")
        return {"message": "File uploaded successfully!", "filename_in_s3":key}
    except botocore.exceptions.ParamValidationError as e:
        return {"error": f"Parameter validation error: {e}"}
    except botocore.exceptions.ClientError as e:
        return {"error": f"Client error: {e}"}
    


@app.get("/audio_files/")
async def processed_files():
    """
    Returns list of all the processed files
    """
    return {"files" : db_helper.processed_files()}


@app.get("/processed_query_result/{file}/{query}")
async def processed_query(file, query):
    """_summary_

    Args:
        query (_type_): Pass the already processed query 
        file (_type_): Pass the file name to be queried 
    """
    
    return {"query_response" : db_helper.processed_query(file, query)}


