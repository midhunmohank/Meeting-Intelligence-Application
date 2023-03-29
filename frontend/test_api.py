# import streamlit as st
# import requests 
# import base64




# host_airflow = 'http://localhost:8000'
# headers_airflow = {
#     "Content-Type": "application/json",
#     "Authorization": "Basic <base64-encoded-username-password>"
# }

# username_airflow = "airflow2"
# password_airflow = "airflow2"
# auth = f"{username_airflow}:{password_airflow}"
# encoded_auth = base64.b64encode(auth.encode()).decode('ascii')
# headers_airflow['Authorization'] = f"Basic {encoded_auth}"

# payload_airflow = {
#                     "conf": {
#                         "bucket_name": "goes-team6",
#                         "file_name": response.json()["filename_in_s3"]
#                     }
#                 }

# response = requests.post(f"{host_airflow}/uploadfile/", headers=headers_airflow, payload=payload_airflow)

# print(response.json())


import requests

# Define the variables
webserver_id = 'YOUR-TENANT-PROJECT' # Replace with your tenant project ID
dag_name = 'ad_hoc' # Replace with the name of your DAG
client_id = 'YOUR-CLIENT-ID' # Replace with your webserver's client ID
webserver_url = f'https://optimal-bivouac-380619.appspot.com/api/v1/dags/ad_hoc/dagRuns'

# Define the payload for the DAG run
payload = {
    'conf': {
        'bucket_name': 'goes-team6',
        'file_name':  'uploads/1680036452.mp3'
    }
}

# Define the headers for the request
headers = {'Authorization': 'Bearer $(gcloud auth print-identity-token)'}

# Send a POST request to the Airflow REST API via IAP to trigger the DAG run
response = requests.post(webserver_url, headers=headers, json=payload)

# Check the response status code
if response.status_code != 200:
    print(f'Error: {response.text}')
else:
    print('DAG run successfully triggered.')