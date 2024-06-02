# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama

# import streamlit as st
# import os
# from dotenv import load_dotenv
# load_dotenv()

# # LangSmith Tracking 
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# # CHAT PROMPT
# prompt = ChatPromptTemplate.from_messages([
#     # {"role": "system", "content": "You are a helpful assistant. Please respond to the queries"},
#     # {"role": "user", "content": "Question : {question}"}
#     ("system","You are a helpful assistant. Please respond to the queries"),
#     ("user", "Question : {question}")
# ])


# # STREAMLIT CODE
# st.title("Langchain Demo with OLLAMA LLAMA3")
# input_text=st.text_input("Search the topic you want")

# # OPEN LLM  
# llm=Ollama(model="llama3");
# output_parser=StrOutputParser()
# chain=prompt|llm|output_parser

# if input_text:
#     st.write(chain.invoke({'question':input_text}))

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv
import time

load_dotenv()

# LangSmith Tracking 
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Define the chat prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the queries"),
    ("user", "Question : {question}")
])

# Initialize the LLM model once to avoid reloading
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Streamlit app
st.title("Langchain Demo with OLLAMA LLAMA3")
input_text = st.text_input("Search the topic you want")

if input_text:
    start_time = time.time()  # Track start time
    response = chain.invoke({'question': input_text})
    end_time = time.time()  # Track end time
    latency = end_time - start_time
    st.write(response)
    st.write(f"Latency: {latency:.2f} seconds")
