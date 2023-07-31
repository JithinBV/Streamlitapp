pip install huggingface_hub
!pip install langchain

import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'

from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

question = "Who won the FIFA World Cup in the year 1994? "

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

repo_id = "google/flan-t5-xxl"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
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

