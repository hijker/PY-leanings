from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from .chat_service import ChatServ

class ChatResponse(BaseModel):
    answer: str
    
class ChatRequest(BaseModel):
    message: str

app = FastAPI()
chat_service = ChatServ()

@app.post("/chat/")
def chat(request: ChatRequest) -> ChatResponse:
    
    # reply = chat_service.get_response(input=message)
    # return ChatResponse(response=reply)
    return StreamingResponse(
        chat_service.get_response(input=request.message),
        media_type="text/plain"
    )