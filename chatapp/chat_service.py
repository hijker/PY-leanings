from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

class ChatServ:
    def get_response(self, input : str) -> str:
        return client.responses.create(
            model="gpt-4o-mini",
            input=input
        )