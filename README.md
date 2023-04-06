# Meeting-Intelligence-Application


INTRODUCTION
The purpose of this report is to describe the architecture and features of a meeting intelligence application that we built using Streamlit, Whisper API, ChatGPT API, Docker, Airflow, GCP, and Snowflake DB. This application is designed to help users analyze and extract insights from meeting recordings. In the following sections, we will describe the architecture and functionality of the application in more detail.

Team Members: Midhun, Sanjay, Snehil, Vikash


#Application Links 

[API Link](http://54.236.17.95:8000/docs) <br>
[Application Link](http://54.236.17.95:8081/) <br>

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
