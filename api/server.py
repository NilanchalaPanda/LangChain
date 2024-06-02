from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"

app=FastAPI(
    title="Langchain Server",
    version="0.0.1",
    description="A simple API Server",
)

# add_routes(
#     app,
#     ChatOpenAI,
#     path="/openai"
# )

model=ChatOpenAI()
llm=Ollama(model="llama3")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words");
prompt2=ChatPromptTemplate.from_template("Give some facts about {topic} like explaining it to a 5 year child");

add_routes(
    app,
    prompt1|model,
    path="/openaiEssay"
)

add_routes(
    app,
    prompt2|llm,
    path="/llamaPoem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=9000)