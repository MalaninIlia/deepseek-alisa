import os
from fastapi import FastAPI, Request
import requests

app = FastAPI()

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@app.post("/")
async def main(request: Request):
    body = await request.json()
    user_text = body["request"]["original_utterance"]

    response = requests.post(
        OPENROUTER_API_URL,
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": "https://alice.yandex.ru",
            "X-Title": "Alisa Skill"
        },
        json={
            "model": "deepseek/deepseek-chat-v3-0324:free",
            "messages": [{"role": "user", "content": user_text}]
        }
    )
