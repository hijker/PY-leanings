from fastapi import FastAPI
from pydantic import BaseModel

from .chat_service import ChatServ

class ChatResponse(BaseModel):
    response: str
    
app = FastAPI()
chat_service = ChatServ()

@app.get("/chat/{message}", response_model = ChatResponse)
def chat(message : str) -> ChatResponse:
    reply = chat_service.get_response(input=message)
    return ChatResponse(response=reply)