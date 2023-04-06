# Meeting-Intelligence-Application


INTRODUCTION
The purpose of this report is to describe the architecture and features of a meeting intelligence application that we built using Streamlit, Whisper API, ChatGPT API, Docker, Airflow, GCP, and Snowflake DB. This application is designed to help users analyze and extract insights from meeting recordings. In the following sections, we will describe the architecture and functionality of the application in more detail.

Team Members: Midhun, Sanjay, Snehil, Vikash


# Application Links 

[API Link](http://54.236.17.95:8000/docs) <br>
[Application Link](http://54.236.17.95:8081/) <br>

# Architecture Diagram
![Architecture](https://raw.githubusercontent.com/BigDataIA-Spring2023-Team06/Documentation/main/meetingint.jpg)

# Project Structure
```
.
├── README.md
├── airflow_ge
│   ├── Dockerfile
│   ├── dags
│   │   ├── __pycache__
│   │   │   ├── ad_hoc.cpython-37.pyc
│   │   │   ├── gpt_helper.cpython-37.pyc
│   │   │   ├── gpt_helper.cpython-38.pyc
│   │   │   └── test_dags.cpython-37.pyc
│   │   ├── ad_hoc.py
│   │   ├── batch.py
│   │   ├── gpt_helper.py
│   │   ├── test_dag.py
│   │   └── test_dags.py
│   ├── docker-compose.yml
│   ├── main.py
│   └── requirements.txt
├── backend
│   ├── Dockerfile
│   ├── db_helper.py
│   ├── file_upload_api.py
│   ├── gpt-testing.py
│   ├── gpt_helper.py
│   ├── readme.md
│   └── requirements.txt
├── docker-compose.yml
└── frontend
    ├── Dockerfile
    ├── helper_functions
    │   └── airflow_restapi_caller.py
    ├── main.py
    ├── requirements.txt
    └── test_api.py

7 directories, 27 files
mohan@midhun Meeting-Intelligence-Application % tree
.
├── README.md
├── airflow_ge
│   ├── Dockerfile
│   ├── dags
│   │   ├── ad_hoc.py
│   │   ├── batch.py
│   │   ├── gpt_helper.py
│   │   ├── test_dag.py
│   │   └── test_dags.py
│   ├── docker-compose.yml
│   ├── main.py
│   └── requirements.txt
├── backend
│   ├── Dockerfile
│   ├── db_helper.py
│   ├── file_upload_api.py
│   ├── gpt-testing.py
│   ├── gpt_helper.py
│   ├── readme.md
│   └── requirements.txt
├── docker-compose.yml
└── frontend
    ├── Dockerfile
    ├── helper_functions
    │   └── airflow_restapi_caller.py
    ├── main.py
    ├── requirements.txt
    └── test_api.py
```

# API Documentation

## Upload File

Endpoint to upload a file to an S3 bucket.

### Request

`POST /uploadfile/`

#### Parameters

- `file`: The file to be uploaded.

#### Response

- `message`: A message indicating the success of the file upload.
- `filename_in_s3`: The name of the uploaded file in the S3 bucket.

## Processed Files

Endpoint to get a list of all the processed files.

### Request

`GET /audio_files/`

#### Response

- `files`: A list of all the processed files.

## Processed Query Result

Endpoint to get the result of a processed query for a given file.

### Request

`GET /processed_query_result/{file}/{query}`

#### Parameters

- `file`: The name of the file to be queried.
- `query`: The query to be processed.

#### Response

- `query_response`: The response to the processed query.

## Custom Query

Endpoint to get the response to a custom query for a given file.

### Request

`GET /custom_query/{file}/{query}`

#### Parameters

- `file`: The name of the file to be queried.
- `query`: The query to be processed.

#### Response

- `query_response`: The response to the custom query.
