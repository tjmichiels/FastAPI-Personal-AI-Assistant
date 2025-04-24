# Commands gebruikt moeten worden voor het opstarten van de LLM

Het redirecten naar de juiste folder
```
cd C:\Users\Gebruiker\PycharmProjects\FastAPI-Personal-AI-Assistant\app\python-backend
```

Het installeren van de juiste packages
```
CD pip install langchain llama-index chromadb fastapi uvicorn
```

Om de LLM local te kunnen runnen op port 80
```
uvicorn app:app --reload
```

Het is aangeraden om de CRUD operations momenteel te doen via Postman aangezien er nog niet een duidelijke connectie is met Vercel.
