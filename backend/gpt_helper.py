import openai
import boto3 


openai.api_key = "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"


s3 = boto3.client(
    's3',
    aws_access_key_id="AKIAZW4EPXNK5AQIEQWO",
    aws_secret_access_key="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",
)


