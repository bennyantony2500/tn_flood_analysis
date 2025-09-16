from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from vector import retriever

model=OllamaLLM(model="llama3.2")

template="""
You are an expert in analysing flood patterns and giving suitable protection.

Here are some relevant reviews: {reviews}

Here is the question: {question}
"""


prompt=ChatPromptTemplate.from_template(template)

chain=prompt | model

while True:
    question=input("Ask question or type 0 to quit")
    if question=="0":
        break

    retrieve=retriever.invoke(question)

    result=chain.invoke({"reviews":retrieve,"question":question})
    print(result)


