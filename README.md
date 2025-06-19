# 🧠 Windi Backend

Dit is de backend van het Windi-project: een lokale, privacygerichte AI-assistent gebouwd met FastAPI, LangChain, Ollama en ChromaDB.

---

## ⚙️ Vereisten

Zorg dat je de volgende software lokaal hebt geïnstalleerd:

* [Python 3.10+](https://www.python.org/downloads/)
* [Ollama](https://ollama.com/) – vereist voor het lokaal draaien van LLMs (zoals LLaMA, Mistral, enz.)
* [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/downloads/?q=build+tools) – nodig voor sommige Python-dependencies

---

## 📦 Installatie en setup

Navigeer naar de juiste backendmap:

```bash
cd C:\Users\<jouw-gebruikersnaam>\PycharmProjects\FastAPI-Personal-AI-Assistant\app\python-backend
```

Installeer de benodigde packages:

```bash
pip install langchain-community llama-index chromadb fastapi uvicorn
```

Herhaal deze stap indien nodig voor extra afhankelijkheden:

```bash
pip install chromadb
pip install langchain-community
```

---

## 🧪 Lokale development server starten

Zorg dat Ollama op de achtergrond draait (bijvoorbeeld met `ollama run mistral` of een ander model), en start dan de backend via:

```bash
uvicorn app:app --reload
```

Of, als alternatief:

```bash
python -m uvicorn app:app --reload
```

De server draait dan lokaal op:
📍 `http://127.0.0.1:8000`

