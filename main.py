from fastapi import FastAPI
from baseModel import ChatRequest
from dotenv import load_dotenv
import os
import openai

app = FastAPI()
load_dotenv()

OPENAI_API_KEY = os.environ.get('API_KEY')

openai.api_key = OPENAI_API_KEY

@app.post("/chat")
def chat_with_ai(request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.message}]
        )
        return {"reply": response["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}