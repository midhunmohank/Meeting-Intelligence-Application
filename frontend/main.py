import streamlit as st

# Set page title
st.set_page_config(page_title="Meeting Intelligence Application")

# Define allowed file types
ALLOWED_EXTENSIONS = {'mp3'}

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
            st.success("File uploaded successfully!")
            # Store the file on cloud or perform further processing
        else:
            st.error("Invalid file type. Please upload an MP3 file.")

# Display home page
home()
