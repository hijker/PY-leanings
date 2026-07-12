from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")

class ChatServ:
    
    
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": "You are a mathematician"
            }
        ]
    
    
    def get_response(self, input : str) -> str:
        
        self.messages.append({
            "role":"user",
            "content" : input
        })
        response = client.responses.create(
            model="llama-3.3-70b-versatile",
            input=self.messages,
            stream=True
        )
        
        answer = ""
        
        for event in response :
            print(event)
            
            if event.type == "response.output_text.delta":
                answer += event.delta
                yield event.delta

            
            
        # print (response.model_dump_json(indent=2))
        self.messages.append({
            "role":"assistant",
            "content" : answer
        })
        return answer