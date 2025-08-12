# ローカルLLM 利用 するための podman compose
Ollama と Open WebUI  

# 初期化
```bash

podman compose up -d

# ollama コンテナに入る
podman compose exec ollama bash
# podman compose exec app bash

# GPU 確認
vulkaninfo | grep GPU

# モデル一覧
ollama list

# モデルをプルする
ollama run llava
# ollama run llama3
# ollama run gemma3:4b
# ollama run gpt-oss:20b

# ホスト名確認
cat /etc/hosts
```

# ログ確認
```bash
podman compose logs ollama
podman compose logs open-webui
```

# 使い方

1. Open WebUI を起動する  

```bash
http://localhost:3000/  
# http://192.168.86.135:3000/  
```

```bash
ID: admin@example.com
パスワード dU3inxfX
```

# モデルの動作確認
```bash
curl "http://localhost:11434/api/chat" -d '{
  "model": "gemma3:4b",
  "messages": [
    {
      "role": "user",
      "content": "こんにちは"
    }
  ],
  "stream": false
}' | jq -r .message.content > example/text.txt

# 音声作成
curl -v -s \
    -X POST \
    "http://localhost:50021/audio_query?speaker=1" \
    --get --data-urlencode text@example/text.txt > example/query.json

curl -v -s \
    -X POST \
    -H "Content-Type: application/json" \
    -d @example/query.json \
    "localhost:50021/synthesis?speaker=1" \
    > example/audio.wav

curl -v -s \
  -X POST \
  -H "Content-Type: application/json" \
  -d @example/chat.json \
  http://localhost:8888/api/chat
```

## 参考

ローカルLLMの使用 - OllamaとOpen WebUIの連携について解説  
https://qiita.com/RyutoYoda/items/ecdfbef8c73aae64aa45

Apple Silicon(M3) Macで Ollama を動かしてみた  
https://zenn.dev/mori2_jp/articles/a6b3b4ba17ac01
