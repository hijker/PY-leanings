from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")

class ChatServ:
    def get_response(self, input : str) -> str:
        response = client.responses.create(
            model="llama-3.3-70b-versatile",
            input=input
        )
        print (response.model_dump_json(indent=2))
        return response.output[1].content[0].text