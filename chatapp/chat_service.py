from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

def get_weather(city: str) -> str:
    weather = {
        "bangalore" : "Sunny, 25C",
        "mumbai": "Couldy, 31C",
        "delhi": "Hot, 37C"
    }
    return weather.get(city.lower(), "City not found")  

tools = [
    {
        "type" : "function",
        "name" : "get_weather",
        "description" : "returns the weather of a give city",
        "parameters" : {
            "type":"object",
            "properties" : {
                "city" : {
                    "type" : "string"
                }
            },
        "required" : ["city"]
        },
    }
]

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")

class ChatServ:
    
    
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": "You are a witty assistant"
            }
        ]
    
    
    def get_response(self, input : str) -> str:
        
        self.messages.append({
            "role":"user",
            "content" : input
        })
        
        answer = ""
        response = client.responses.create(
            model="llama-3.3-70b-versatile",
            input=self.messages,
            # stream=True,
            tools=tools
        )
        print(response.model_dump_json(indent=2))
        
        tool_call = response.output[1]
        
        # print(json.dumps(response,indent=2))

        args = json.loads(tool_call.arguments)
        
        result = get_weather(args["city"])
        
        response = client.responses.create(
            model="llama-3.3-70b-versatile",
            previous_response_id=response.id,
            input=[
                {
                    "type" : "tool_call_response",
                    "call_id": tool_call.call_id,
                    "output" : result
                }
            ],
            # stream=True,
            tools=tools
        )
        
        # for event in response :
        #     # print(event)
            
        #     if event.type == "response.output_text.delta":
        #         answer += event.delta
        #         yield event.delta

            
            
        # print (response.model_dump_json(indent=2))
        self.messages.append({
            "role":"assistant",
            "content" : answer
        })
        return answer