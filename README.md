# Commands gebruikt moeten worden voor het opstarten van de LLM

Het redirecten naar de juiste folder
```
cd C:\Users\Gebruiker\PycharmProjects\FastAPI-Personal-AI-Assistant\app\python-backend
```

Het installeren van de juiste packages
```
CD pip install langchain llama-index chromadb fastapi uvicorn
```

Het installeren van de langchain package
```
pip install langchain-community
```

Om de LLM local te kunnen runnen op port 8000
```
uvicorn app:app --reload
```

Het is aangeraden om de CRUD operations momenteel te doen via Postman aangezien er nog niet een duidelijke connectie is met Vercel. 

Ook is het belangrijk om [Microsoft C++ VS Build Tools](https://visualstudio.microsoft.com/downloads/?q=build+tools) te hebben geinstalleerd op je laptop 

