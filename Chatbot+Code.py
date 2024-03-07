import os
import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv




# OPENAI_API_KEY = "sk-PHzh89333124kjfd38493jjfdk84035i5Z" #Pass your key here
OPENAI_API_KEY = os.getenv("API_KEY")

#Upload PDF files
st.header("My first Chatbot")

with  st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader(" Upload a PDf file and start asking questions", type="pdf")

#Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        st.write(text)
