# Importing required packages

import openai

import boto3

import json




# Whisper API_KEY

openai.api_key = "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"




# takes bucket_name, folder_name, file_name as input and returns the transcript

def generate_txt_file(bucket_name, folder_name, file_name):

    s3 = boto3.client('s3', region_name = 'us-east-1')

    response = s3.get_object(Bucket=bucket_name, Key=f"{folder_name}/{file_name}")

    audio_key = f"{folder_name}/{file_name}"

    audio_file = s3.download_file(bucket_name, audio_key, '/tmp/audio_file.mp3')




    # Transcribe the audio using the Whisper API

    transcript = openai.Audio.transcribe("whisper-1", open('/tmp/audio_file.mp3', 'rb'))

    transcript = transcript.to_dict()

    return transcript

    




generated_transcript = generate_txt_file('meetingintelligence','adhocprocess', 'Small_Talk.mp3')

print(generated_transcript)




def upload_txt_to_s3(bucket_name, folder_name, file_name, text_content):

    s3 = boto3.client('s3', region_name='us-east-1')




    # Write text content to a file

    file_path = '/tmp/transcript.txt'

    with open(file_path, 'w') as f:

        f.write(text_content)




    # Upload text file to S3 bucket

    s3.upload_file(file_path, bucket_name, f"{folder_name}/{file_name}")




# print(upload_txt_to_s3('meetingintelligence', 'processedtext/', 'proccessed_text.txt', generated_transcript['text']))