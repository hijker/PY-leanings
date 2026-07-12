from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Hello I'm home"

@app.get("/hello/{name}")
def greet(name: str):
    return "Hello " + name

@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    return num1 + num2

# starts using uvicron api.simpleapi:app --reload
