# import os
# import json
# import openai
# import boto3
# from airflow.models import DAG
# from airflow.operators.bash import BashOperator
# from airflow.operators.python import PythonOperator
# from airflow.utils.dates import days_ago
# from airflow.models.param import Param
# from datetime import timedelta, datetime
# import snowflake.connector

# openai.api_key = "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"

# s3 = boto3.client(
#     's3',
#     aws_access_key_id="AKIAZW4EPXNK5AQIEQWO",
#     aws_secret_access_key="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",
# )

# print(s3.get_object(Bucket="goes-team6", Key="test-rec.mp3"))

# #########Function to generate transcript 
# def generate_txt_file(bucket_name, file_name):
#     #s3 = boto3.client('s3', region_name = 'us-east-1')
#     response = s3.get_object(Bucket=bucket_name, Key=f"{file_name}")
#     audio_key = f"{file_name}"
#     audio_file = s3.download_file(bucket_name, audio_key, '/tmp/audio_file.mp3')
#     # Transcribe the audio using the Whisper API
#     transcript = openai.Audio.transcribe("whisper-1", open('/tmp/audio_file.mp3', 'rb'))
#     transcript = transcript.to_dict()
#     return transcript

# # Function to call GPT API with a message 
# def get_response_gpt(message):
#     response =  openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo", 
#         messages = [
#             {"role" : "user", "content" : message}
#         ]
#     )
#     return response

# # Function to extract the reply from the response body og GPT API
# def get_reply(response):
#     return response['choices'][0]['message']['content'] 

# # Function to establish connection with snowflake
# def create_connection():
#     conn = snowflake.connector.connect(
#         user='SANJAYKASHYAP',
#         password='Bigdata@23',
#         account='iogoldm-vcb38713',
#         warehouse='COMPUTE_WH',
#         database='INTEL_MEETING',
#         schema='PUBLIC'
#     )
#     return conn