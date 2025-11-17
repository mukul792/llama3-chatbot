import os
import streamlit as st
from dotenv import load_dotenv

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant, answer to the question asked" ),
        ("user","question:{question}")
    ]
)

st.title("langchain demo with llama 3.1 open source model")
input_text = st.text_input("What's your question ?")

llm = Ollama(model="llama3.1:latest")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))