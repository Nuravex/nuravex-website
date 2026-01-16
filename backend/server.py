from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain.messages import HumanMessage
from cs_agent.app.agent.graph import support_agent
from cs_agent.app.schemas.messages import user_message
from fastapi.responses import JSONResponse

app = FastAPI(title="cs agent backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ChatRequest(BaseModel):
    question:str
    
@app.get('/')
def root():
    return {'ststus':'Backend running'}

@app.post("/chat")
async def chat(request: ChatRequest):
    print("QUESTION RECEIVED:", request.question)
    question = request.question
    state = {
        "messages":[user_message(question)]
    }
    result = support_agent.invoke(state)
    ai_response = result["messages"][-1].content
    return JSONResponse({"response": result["messages"][-1].content})