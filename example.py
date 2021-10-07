import streamlit as st
import os

# Only supports JPG and PNG atm

st.header("Upload and processing")
st.write("Small example of image-statistics for the data quality wrapper")
uploaded_files = st.file_uploader('Select files',type=['png','jpg','zip'],accept_multiple_files=True)
file_lst = [uploaded_file.name for uploaded_file in uploaded_files]
if st.button("Process"):
    st.write("All files uploaded")
    if file_lst is not None:
        for file in uploaded_files:
            file_details = {"Filename":file.name,"FileType": file.type,"FileSize":file.size}
            st.write(file_details)








# number of images

# average pixels

# average colour