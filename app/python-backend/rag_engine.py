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

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    # 🔁 Vectorstore realtime opbouwen (optioneel, of gebruik persistent)
    vectorstore = Chroma.from_documents(
        chunks,
        embedding=OllamaEmbeddings(),
        persist_directory="chroma_db"
    )

    # Haal tot 8 stukken context op
    retriever = vectorstore.as_retriever(search_kwargs={"k": 8})
    relevant_docs = retriever.get_relevant_documents(question)

    # 🔍 Debug: print welke context is opgehaald
    print("\n🔍 [DEBUG] Opgehaalde context:\n")
    for i, doc in enumerate(relevant_docs):
        print(f"📄 Context {i+1}:\n{doc.page_content}\n-----------")

    # Prompt in het Nederlands, geen fantasie
    prompt = PromptTemplate.from_template(
        "Je bent een vriendelijke studiecoach aan Windesheim. "
        "Gebruik alleen de onderstaande context om de vraag in het Nederlands te beantwoorden. "
        "Als je het antwoord niet kunt vinden in de context, zeg dan: 'Sorry, ik heb hier geen informatie over.'\n\n"
        "Context:\n{context}\n\nVraag:\n{question}\n\nAntwoord:"
    )

    llm = Ollama(model="llama3")
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa.run(question)
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

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    # 🔁 Vectorstore realtime opbouwen (optioneel, of gebruik persistent)
    vectorstore = Chroma.from_documents(
        chunks,
        embedding=OllamaEmbeddings(),
        persist_directory="chroma_db"
    )

    # Haal tot 8 stukken context op
    retriever = vectorstore.as_retriever(search_kwargs={"k": 8})
    relevant_docs = retriever.get_relevant_documents(question)

    # 🔍 Debug: print welke context is opgehaald
    print("\n🔍 [DEBUG] Opgehaalde context:\n")
    for i, doc in enumerate(relevant_docs):
        print(f"📄 Context {i+1}:\n{doc.page_content}\n-----------") # Dit was een en al voor testing bedoeld 

    # Prompt in het Nederlands, geen fantasie
    prompt = PromptTemplate.from_template(
        "Je bent een vriendelijke studiecoach aan Windesheim. "
        "Gebruik alleen de onderstaande context om de vraag in het Nederlands te beantwoorden. "
        "Als je het antwoord niet kunt vinden in de context, zeg dan: 'Sorry, ik heb hier geen informatie over.'\n\n"
        "Context:\n{context}\n\nVraag:\n{question}\n\nAntwoord:"
    )

    llm = Ollama(model="llama3")
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa.run(question)
