from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

data_dir = Path("docs")
docs = []
for path in data_dir.rglob("*.pdf"):
    loaded_docs = PyPDFLoader(str(path)).load()
    for doc in loaded_docs:
        doc.metadata["filename"] = path.name
    docs.extend(loaded_docs)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300, 
    chunk_overlap=50
    )

chunks = splitter.split_documents(docs)
print(f"Total de chunks: {len(chunks)} total de arrays: {len(docs)}")

embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-small")
vector_store = FAISS.from_documents(chunks, embeddings)
vector_store.save_local("vectorstore")
print(f"indexados: {len(vector_store.index_to_docstore_id)} chunks")







