from contextlib import nullcontext
import streamlit as st
from csv_reader import readcsv

st.header('Single File Upload')
uploaded_file = st.file_uploader('Upload a file')

st.write(readcsv(uploaded_file))