from fastapi import FastAPI, Request
from rag_engine import get_rag_answer

app = FastAPI()

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data["question"]
    answer = get_rag_answer(question)
    return {"answer": answer}
