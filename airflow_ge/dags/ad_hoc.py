import openai
import boto3 
import airflow
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models.param import Param
from datetime import timedelta, datetime
import snowflake.connector

openai.api_key = ""


s3 = boto3.client(
    's3',
    aws_access_key_id="",
    aws_secret_access_key="",
)


# Function to call GPT API with a message 
def get_response_gpt(message):
    response =  openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", 
        messages = [
            {"role" : "user", "content" : message}
        ]
    )
    return response


# Function to establish connection with snowflake
def create_connection():
    conn = snowflake.connector.connect(
        user='CHATGPT',
        password='',
        account='pigjtsl-ed61481',
        warehouse='COMPUTE_WH',
        database='INTEL',
        schema='PUBLIC'
    )
    return conn



#########Function to generate transcript 
def generate_txt_file(bucket_name, file_name, file_name_trans):
    s3.download_file(bucket_name, f'uploads/{file_name}', '/tmp/audio_file.mp3')
    # Transcribe the audio using the Whisper API
    transcript = openai.Audio.transcribe("whisper-1", open('/tmp/audio_file.mp3', 'rb'))
    transcript = transcript.to_dict()
    # Upload text file to S3 bucket    
    file_path = '/tmp/transcript.txt'
    with open(file_path, 'w') as f:
        f.write(transcript["text"])
    s3.upload_file(file_path, bucket_name, f"transcripts/{file_name_trans}")

    return transcript

# transcript = {"text":"This is a dummy text. Hello from airflow"}
#     # Upload text file to S3 bucket    
# file_path = '/tmp/transcript.txt'
# with open(file_path, 'w') as f:
#     f.write(transcript["text"])
# s3.upload_file(file_path, 'goes-team6', f"transcripts/test-file-from-python.txt")

def send_query(audio_file, transcript):
    
    response_summary = get_response_gpt(f"Give me a summary of the following meeting transcript {transcript}")
    response_tone  = get_response_gpt(f"Provide some feedback on the nature of the discussion the tone of the attendees in this meeting from the transcript {transcript}")
    response_language = get_response_gpt(f"List the languages used in this meeting transcript {transcript}")
    summary = response_summary["choices"][0]["message"]["content"].replace("'", "") 
    tone = response_tone["choices"][0]["message"]["content"].replace("'", "")
    language = response_language["choices"][0]["message"]["content"].replace("'", "")
    query = f"INSERT INTO QUERY_RESULTS (AUDIO_FILE, SUMMARY, TONE, LANGUAGE, UPLOADED_AT) VALUES ('{audio_file}', '{summary}', '{tone}', '{language}', CURRENT_TIMESTAMP);"
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    return response_summary
    

dag = DAG(
    dag_id="ad_hoc",
    schedule= "0 0 * * *",
    start_date= days_ago(0),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=["ad_hoc"]
)

with dag:
    
    get_transcript = PythonOperator(
        task_id="get_transcript",
        python_callable=generate_txt_file,
        op_kwargs={"bucket_name":"goes-team6", "file_name":'{{ dag_run.conf["file_name"] }}', "file_name_trans": '{{ dag_run.conf["file_name_trans"] }}'} ,       
        provide_context=True,

    )

    send_query = PythonOperator(
        task_id="send_query",
        python_callable=send_query, 
        op_kwargs={
            'audio_file': '{{ dag_run.conf["file_name"] }}',
            "transcript": "{{ task_instance.xcom_pull(task_ids='get_transcript', key='return_value') }}"
        },
        provide_context=True,

    )

    # Add a dependency between the tasks
    get_transcript >> send_query
    
    



