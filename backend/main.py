from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)

class ChatRequest(BaseModel):
    question:str

@app.post("/chat")
async def chat(request: ChatRequest):
    question = request.question
    # For now, just echo the question (placeholder)
    return {"answer": f"You asked: {question}"}