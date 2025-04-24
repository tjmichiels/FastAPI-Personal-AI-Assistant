from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os

def load_documents():
    docs = []
    for filename in os.listdir("docs"):
        if filename.endswith(".txt"):
            path = os.path.join("docs", filename)
            loader = TextLoader(path, encoding="utf-8")
            docs.extend(loader.load())
    return docs

def get_rag_answer(question):
    docs = load_documents()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(
        chunks,
        embedding=OllamaEmbeddings(),
        persist_directory="chroma_db"
    )

    retriever = vectorstore.as_retriever()

    prompt = PromptTemplate.from_template(
        "Je bent een vriendelijke studentenbegeleider. Beantwoord de vraag in het Nederlands en gebruik alleen de context hieronder.\n\nContext:\n{context}\n\nVraag:\n{question}\n\nAntwoord:"
    )

    llm = Ollama(model="llama3")
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa.run(question)
