import os
from dotenv import load_dotenv
from rich import print
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model=os.getenv("GROQ_MODEL"))

print(llm.invoke("Estou testando LangSmith neste momento"))




