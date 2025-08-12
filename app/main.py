import os
import re
import asyncio
import json
import uuid
import logging
import threading
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from ollama import AsyncClient

from voicevox import Voicevox

FAST_API_PORT = 8888

# 環境変数 読み込み
HOST_IP = os.environ.get("HOST_IP")

OLLAMA_MODEL = "gemma3:4b"
OLLAMA_HOST_URL =f'http://{HOST_IP}:11434'

ollamaClient = AsyncClient(host=OLLAMA_HOST_URL)

# ロガー設定
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# FastAPI を初期化します
fast_api = FastAPI()
origins = [ "http://localhost", "http://localhost:{FAST_API_PORT}" ]
fast_api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

voicevox = Voicevox(f'http://{HOST_IP}:50021', 1)

@fast_api.get("/api/media-file/{uuid_str}")
async def post_media_file(uuid_str: str):
    audio_path = f"static/output_{uuid_str}.wav"
    return FileResponse(audio_path, media_type="audio/wav")

async def dummy_chat():
    response = await ollamaClient.chat(model=OLLAMA_MODEL, messages=[
        {
            'role': 'user',
            'content': 'こんにちは',
        },
    ])

    # query = await voicevox.audio_query(response.message.content)
    # # logger.info(f"Audio query: {query}")
    # ret = await voicevox.synthesize(query)
    # # 音声データをファイルに保存
    # uuid_str = str(uuid.uuid4())
    # audio_path = f"static/output_{uuid_str}.wav"
    # with open(audio_path, "wb") as f:
    #     f.write(ret)

    # 音声データのパスを返す
    return {"message": response.message.content}

@fast_api.get("/api/dummy")
async def dummy():
    response = await dummy_chat()
    return response

class ChatRequest(BaseModel):
    system: str
    user: str
    assistant: str
    
async def chat(req: ChatRequest):
    response = await ollamaClient.chat(model=OLLAMA_MODEL, messages=[
        {
            "role": "system",
            "content": req.system,
        },
        {
            'role': 'user',
            'content': req.user,
        },
        {
        "role": "assistant",
        "content": req.assistant
        }        
    ])

    query = await voicevox.audio_query(response.message.content)
    # logger.info(f"Audio query: {query}")
    ret = await voicevox.synthesize(query)
    # 音声データをファイルに保存
    uuid_str = str(uuid.uuid4())
    audio_path = f"static/output_{uuid_str}.wav"
    with open(audio_path, "wb") as f:
        f.write(ret)
    # 音声データのパスを返す
    return {"message": response.message.content, "audio": f"http://{HOST_IP}:{FAST_API_PORT}/api/media-file/{uuid_str}"}

@fast_api.post("/api/chat")
async def api_chat(req: ChatRequest):    
    return await chat(req)

def fast_api_run():
    uvicorn.run(fast_api, host="0.0.0.0", port=FAST_API_PORT)

# アプリを起動します
if __name__ == "__main__":
    thread1 = threading.Thread(target=fast_api_run)
    thread1.start()
