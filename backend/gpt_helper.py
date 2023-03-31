import openai
import boto3 


openai.api_key = "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"


s3 = boto3.client(
    's3',
    aws_access_key_id="AKIAZW4EPXNK5AQIEQWO",
    aws_secret_access_key="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",
)

bucket = 'goes-team6'

####Funtion to get the text file 

def read_s3_text_file(bucket_name, file_key):
    # Create an S3 client
    # s3 = boto3.client('s3')
    
    # Read the file contents from S3
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = response['Body'].read().decode('utf-8')
    
    # Return the file contents as a string
    return file_content

def get_response_gpt(file_name, message):
    
    text = read_s3_text_file(bucket, f'transcripts/{file_name}')
    response =  openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", 
        messages = [
            {"role" : "user", "content" : f"{message} answer this according to this text: {text}" }
        ]
    )
    return response["choices"][0]["message"]["content"]


# print(read_s3_text_file('goes-team6', 'transcripts/1680149857.txt'))

# print(get_response_gpt('1680149857.txt', "Does this have reference to Karnataka"))

