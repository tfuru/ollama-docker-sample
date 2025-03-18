# ローカルLLM 利用 するための docker compose
Ollama と Open WebUI  

# 初期化
```bash
docker compose up -d

# ollama コンテナに入る
docker compose exec ollama bash
# docker compose exec open-webui bash

# モデルをプルする
ollama run llava
# ollama run llama3
# ollama run gemma

# ホスト名確認
cat /etc/hosts
```

# ログ確認
```bash
docker compose logs ollama
docker compose logs open-webui
```


# 使い方

1. Open WebUI を起動する  

```bash
open http://llm-server.local:3000/
# http://localhost:3000/  
# http://192.168.86.135:3000/  
```

```bash
ID: admin@example.com
パスワード dU3inxfX
```

# モデルの動作確認
```bash
docker compose logs ollama

curl http://llm-server.local:11434/api/chat -d '{
  "model": "llama3",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
  "stream": false
}'

curl http://llm-server.local:11434/api/chat -d '{
  "model": "llava",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
  "stream": false
}'

```

```bash
MODEL=llava
BASE64=$(base64 -i ./example/0.jpg)
BASE64=$(base64 -i ./example/1.jpg)
BASE64=$(base64 -i ./example/2.jpg)

echo '{
  "model": "'$MODEL'",
  "stream": false,
  "response_format": {"type": "json_object"},
  "messages": [
    {
      "role": "user",
      "content": "What is in this photo?",
      "images": ["'$BASE64'"]
    },
    {
      "role": "system",
      "content": "Please output the recognized information in accordance with the following JSON schema. {items: [{label: string, score: number}]}"
    },
    {
      "role": "system",
      "content": "Make label a short string."
    },
    {
      "role": "system",
      "content": "Please write the content in Japanese"
    }    
  ]
}' | jq -c > ./example/template.json

curl http://llm-server.local:11434/api/chat -d @./example/template.json | jq -r '.message.content' > ./example/out.json

curl http://192.168.137.1:11434/api/chat -d @./example/template.json | jq -r '.message.content' > ./example/out.json

```

## 参考

ローカルLLMの使用 - OllamaとOpen WebUIの連携について解説  
https://qiita.com/RyutoYoda/items/ecdfbef8c73aae64aa45

Apple Silicon(M3) Macで Ollama を動かしてみた  
https://zenn.dev/mori2_jp/articles/a6b3b4ba17ac01
