from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import ollama

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str
    model: str = 'llama3'  # optioneel mee te geven, default = llama3

@router.post("/chat")
async def chat(req: ChatRequest):
    try:
        response = ollama.chat(
            model=req.model,
            messages=[
                {"role": "user", "content": req.prompt}
            ]
        )
        return {"response": response['message']['content']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))