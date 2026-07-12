from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from .chat_service import ChatServ

class ChatResponse(BaseModel):
    response: str
    
app = FastAPI()
chat_service = ChatServ()

@app.get("/chat/{message}")
def chat(message : str) -> StreamingResponse:
    
    # reply = chat_service.get_response(input=message)
    # return ChatResponse(response=reply)
    return StreamingResponse(
        chat_service.get_response(input=message),
        media_type="text/plain"
    )