import os
from dotenv import load_dotenv
from rich import print
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(model=os.getenv("GROQ_MODEL"), temperature=0.4)
prompt = ChatPromptTemplate.from_template(
    "Você é um assistente de IA que responde a perguntas de forma clara e concisa. " 
    "Pergunta: {question}"
)

def chamar_llm(texto):
    chain = prompt | llm
    resultado = chain.invoke({"question": texto})
    return resultado.content

if __name__ == "__main__":
    print(chamar_llm("Olá LangSmith!"))




