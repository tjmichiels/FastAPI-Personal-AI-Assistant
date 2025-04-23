from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

def get_rag_answer(question):
    llm = Ollama(model="llama3")
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=OllamaEmbeddings())
    retriever = vectorstore.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa.run(question)
