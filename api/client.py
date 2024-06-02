import requests
import streamlit as st

def get_llama_response(input_text):
    response=requests.post("http://localhost:9000/llamaPoem/invoke",
    json={"input":{'topic': input_text}})

    return response.json()['output']

st.title("Langchian with LANGSERVE & FastAPI")
input_text=st.text_input("Learn Facts")

if(input_text):
    st.write(get_llama_response(input_text))