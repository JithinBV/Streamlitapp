#!pip install huggingface_hub
#!pip install langchain


def main():
  st.title("question and answer app")

  question=st.text_input("what is your question?")


  if st.button("Get answer"):
    with st.spinner("Generation Answer..."):
      response=llm_chain.run(question)
    st.success(response)

if __name__=='__main__':
  main()

