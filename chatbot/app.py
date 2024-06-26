from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("LANGCHAIN_API_KEY:", os.getenv("LANGCHAIN_API_KEY"))

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

# LangSmith Tracking 
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


# CHAT PROMPT
prompt = ChatPromptTemplate.from_messages([
    # {"role": "system", "content": "You are a helpful assistant. Please respond to the queries"},
    # {"role": "user", "content": "Question : {question}"}
    ("system","You are a helpful assistant. Please respond to the queries"),
    ("user", "Question : {question}")
])


# STREAMLIT CODE
st.title("Langchain Demo with OPENAI API")
input_text=st.text_input("Search the topic you want")


# OPEN LLM
llm=ChatOpenAI(model="gpt-3.5-turbo");
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))