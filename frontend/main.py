import streamlit as st
import requests 
import base64
from helper_functions import airflow_restapi_caller as arc

# Set page title
st.set_page_config(page_title="Meeting Intelligence Application")

# Define allowed file types
ALLOWED_EXTENSIONS = {'mp3'}

host = 'http://localhost:8000'
headers = {'accept': 'application/json'}

host_airflow = 'http://localhost:8080'
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
                st.write(response.json()["filename_in_s3"])
                conf= {
                    "bucket_name": "goes-team6",
                    "file_name": response.json()["filename_in_s3"], 
                    "file_name_trans" : response.json()["filename_in_s3"].replace("mp3", "txt")
                }
                response_airflow = arc.trigger_dag(dag_id='ad_hoc',data =conf)

                # response_airflow = requests.post(f"{host_airflow}/api/v1/dags/ad_hoc/dagRuns", headers=headers_airflow, json=payload_airflow)
                st.write(response_airflow.json())
                
                if response_airflow.status_code == 200:
                    st.success("Summerizing Complete!")
            # Store the file on cloud or perform further processing
        else:
            st.error("Invalid file type. Please upload an MP3 file.")
            
    # Define question section
    st.write("## Ask a question")
    processed_files = requests.get(f"{host}/audio_files/").json()["files"]        
    selected_file = st.selectbox("Select an uploaded file", processed_files, key="uploaded_files")
    st.write(f"The selected file is {selected_file}")
    # Define question input
    questions = ["Summary of the audio", "Languages used in the audio", "Tone of the audio", "Custom question"]
    question_type = st.selectbox("Select a question type", questions)
    
    if question_type == "Custom question":
        question = st.text_input("Enter a question related to the uploaded file")
        
        
    elif question_type == "Summary of the meeting":
        st.write(requests.get(f'{host}/processed_query_result/{selected_file}/SUMMARY').json()["query_response"])
        
    
    elif question_type == "Languages used in the audio":
        st.write(requests.get(f'{host}/processed_query_result/{selected_file}/LANGUAGE').json()["query_response"])
        
    elif question_type == "Tone of the audio":
        st.write(requests.get(f'{host}/processed_query_result/{selected_file}/TONE').json()["query_response"])

        
    
    # Define submit button
    # if file and question_type:
    #     if st.button("Go"):
    #         st.write("### Results")
    #         st.write(f"You asked: **{question}**")
    #         st.write("Dummy text box")

# Display home page
home()

