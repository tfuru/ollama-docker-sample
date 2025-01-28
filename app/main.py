import os
import re
import logging
import json
import threading

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import ollama
OLLAMA_MODEL = "llama3:latest"

def dummy_chat():
    # response = ollama.generate(model=OLLAMA_MODEL, prompt="Who are you?")
    response = ollama.chat(model=OLLAMA_MODEL, messages=[
        {
            'role': 'user',
            'content': 'Hello',
        },
    ])
    # print(response['message']['content'])
    # print(response.message.content)
    return response

# 環境変数 読み込み
# DUMMY = os.environ.get("DUMMY")

# ロガー設定
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# FastAPI を初期化します
fast_api = FastAPI()
origins = [ "http://localhost", "http://localhost:8080" ]
fast_api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@fast_api.get("/api/dummy")
async def dummy():
    response = dummy_chat()
    return response
    # return {"message": response}
    # return {"message": "dummy"}

def fast_api_run():
    uvicorn.run(fast_api, host="0.0.0.0", port=8000)

# アプリを起動します
if __name__ == "__main__":
    thread1 = threading.Thread(target=fast_api_run)
    thread1.start()
