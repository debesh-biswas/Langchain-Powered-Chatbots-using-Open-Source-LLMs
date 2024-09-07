from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
## langsmith tracking
os.environ["LANGCAHIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##prompt template
propmt = ChatPromptTemplate.from_messages(
    [
        ("system"," you are a helpful assistant. Please respond to the queries!"),
        ("user","Question:{question}")
    ]
)


## Streamlit framework
st.title("Langchain demo using LLAMA2")
input_text = st.text_input("Search a topic")


## Ollama llama2 LLM
llm=Ollama(model = "llama2")
output_parser = StrOutputParser()
chain = propmt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))