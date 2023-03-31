import openai   
import boto3 
import airflow
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models.param import Param
from datetime import timedelta, datetime
import ast


openai.api_key = ""


s3 = boto3.client(
    's3',
    aws_access_key_id="",
    aws_secret_access_key="",
)


#Function to check for fudio file in S3 bucket
def check_file(bucket_name):
    response = s3.list_objects_v2(Bucket=bucket_name)
    names= []
    if 'Contents' in response:
        for item in response['Contents']:
            if item['Key'].startswith('uploads/'):
                names.append(item['Key'].split('/')[1])
    else:
        return None
    print
    return names
    
#########Function to generate transcript 
def generate_txt_file(file_names):
    print(file_names)
    file_names = ast.literal_eval(file_names)
    bucket_name = 'goes-team6'
    for i in ([*range(len(file_names))]):
        file_name = file_names[i]
        print(file_name)
        file_name_trans = file_name.split('.')[0] + '.txt'
        print(file_name_trans)
        s3.download_file(bucket_name, f'uploads/{file_name}', '/tmp/audio_file.mp3')
        # Transcribe the audio using the Whisper API
        transcript = openai.Audio.transcribe("whisper-1", open('/tmp/audio_file.mp3', 'rb'))
        transcript = transcript.to_dict()
        # Upload text file to S3 bucket    
        file_path = '/tmp/transcript.txt'
        with open(file_path, 'w') as f:
            f.write(transcript["text"])
        s3.upload_file(file_path, bucket_name, f"transcripts/{file_name_trans[i]}")


dag = DAG(
    dag_id="batch_processing",
    schedule= "0 0 * * *",
    start_date= days_ago(0),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=["batch"]
)

with dag:
    
    check_file = PythonOperator(
        task_id="check_file",
        python_callable=check_file,
        op_kwargs={'bucket_name': 'goes-team6'},
        dag=dag
    )

    generate_txt_file = PythonOperator(
        task_id="generate_txt_file",
        python_callable=generate_txt_file,
        op_kwargs={'file_names': "{{ task_instance.xcom_pull(task_ids='check_file', key='return_value') }}"},
        dag=dag
    )
    
    check_file >> generate_txt_file
    
    



