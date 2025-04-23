from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def get_rag_answer(question):
    llm = Ollama(model="llama3")

    # Vectorstore ophalen
    vectorstore = Chroma(
        persist_directory="./chroma_db",
        embedding_function=OllamaEmbeddings()
    )
    retriever = vectorstore.as_retriever()

    # Prompt template in het Nederlands
    prompt = PromptTemplate.from_template(
        "Je bent een vriendelijke studiecoach die studenten helpt bij persoonlijke en studie-gerelateerde vragen. "
        "Gebruik de onderstaande context om de vraag in het Nederlands te beantwoorden.\n\n"
        "Context:{context}\n\n"
        "Vraag:\n{question}\n\n"
        "Antwoord:"
    )

    # Retrieval chain met custom prompt
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa.run(question)
