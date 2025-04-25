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

    splitter = CharacterTextSplitter(chunk_size=1200, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(
        chunks,
        embedding=OllamaEmbeddings(),
        persist_directory="chroma_db"
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
    relevant_docs = retriever.get_relevant_documents(question)

    print("\n🔍 [DEBUG] Opgehaalde context:\n")
    for i, doc in enumerate(relevant_docs):
        print(f"📄 Context {i+1}:\n{doc.page_content}\n-----------")

    prompt = PromptTemplate.from_template(
        "Je bent een vriendelijke studiecoach aan Windesheim. "
        "Beantwoord de vraag in het Nederlands op basis van de onderstaande context. "
        "Gebruik geen externe kennis of aannames. "
        "Als je het antwoord niet kunt vinden in de context, zeg dan: 'Sorry, ik heb hier geen informatie over.'\n\n"
        "Context:\n{context}\n\n"
        "Vraag:\n{question}\n\n"
        "Antwoord:"
    )

    llm = Ollama(model="llama3")
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa.run(question)
