
import databutton as db

import streamlit as st
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain


import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'
repo_id = "google/flan-t5-xxl"

question = "Who won the FIFA World Cup in the year 1994? "

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 1264}
)
llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.run(question))

def main():
  st.title("question and answer app")

  question=st.text_input("what is your question?")


  if st.button("Get answer"):
    with st.spinner("Generation Answer..."):
      response=llm_chain.run(question)
    st.success(response)
    


if __name__=='__main__':
  main()
