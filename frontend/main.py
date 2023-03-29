import streamlit as st
import requests 
import base64

# Set page title
st.set_page_config(page_title="Meeting Intelligence Application")

# Define allowed file types
ALLOWED_EXTENSIONS = {'mp3'}

host = 'http://localhost:8000'
headers = {'accept': 'application/json'}

host_airflow = 'service-417868509081@gs-project-accounts.iam.gserviceaccount.com'
headers_airflow = {
    "Content-Type": "application/json",
    "Authorization": "Basic <base64-encoded-username-password>"
}

username_airflow = "airflow2"
password_airflow = "airflow2"
auth = f"{username_airflow}:{password_airflow}"
encoded_auth = base64.b64encode(auth.encode()).decode('ascii')
headers_airflow['Authorization'] = f"Basic {encoded_auth}"


# Define function to check file type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Create home page
def home():
    st.title("Meeting Intelligence Application")
    st.write("Please upload an MP3 file:")
    file = st.file_uploader("", type=["mp3"])
    if file is not None:
        if allowed_file(file.name):
            files = {"file": file.getvalue()}
            # Call the API
            response = requests.post(f"{host}/uploadfile/", headers=headers, files=files)
            
            if response.status_code == 200:
                st.success("File uploaded successfully to S3 bucket. Creating Transcriot and running GPT on it!")
                response.json()["filename_in_s3"]
                payload_airflow = {
                    "conf": {
                        "bucket_name": "goes-team6",
                        "file_name": response.json()["filename_in_s3"]
                    }
                }
                
                response_airflow = requests.post(f"{host_airflow}/api/v1/dags/ad_hoc/dagRuns", headers=headers_airflow, json=payload_airflow)
                st.write(response_airflow.json())
                
                if response_airflow.status_code == 200:
                    st.success("Summerizing Complete!")
            # Store the file on cloud or perform further processing
        else:
            st.error("Invalid file type. Please upload an MP3 file.")

# Display home page
home()


