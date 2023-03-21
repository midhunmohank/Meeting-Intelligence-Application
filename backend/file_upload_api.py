from fastapi import FastAPI, File, UploadFile
import boto3
import botocore
import os

app = FastAPI()

# Define your S3 credentials

aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
s3_bucket = os.environ.get('S3_BUCKET')
region_name = os.environ.get('S3_REGION')

# Create a new S3 client
s3 = boto3.client('s3', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    """
    Uploads a file to an S3 bucket.
    """
    try:
        # Create a key for the file in the S3 bucket
        key = f"uploads/{file.filename}"
        
        # Upload the file to S3
        s3.upload_fileobj(file.file, s3_bucket, key)
        return {"message": "File uploaded successfully!"}
    except botocore.exceptions.ParamValidationError as e:
        return {"error": f"Parameter validation error: {e}"}
    except botocore.exceptions.ClientError as e:
        return {"error": f"Client error: {e}"}
    
@app.get("/downloadfile/{file_name}")
async def download_file(file_name: str, response: Response):
    """
    Downloads a file from an S3 bucket.
    """
    try:
        # Create a key for the file in the S3 bucket
        key = f"uploads/{file_name}"
        
        # Download the file from S3
        response.headers["Content-Disposition"] = f"attachment; filename={file_name}"
        s3.download_fileobj(S3_BUCKET, key, response.body)
        return response
    except botocore.exceptions.ParamValidationError as e:
        return {"error": f"Parameter validation error: {e}"}
    except botocore.exceptions.ClientError as e:
        return {"error": f"Client error: {e}"}
