# ローカルLLM 利用 するための docker compose
Ollama と Open WebUI  

# 初期化
```bash
docker compose up -d

# ollama コンテナに入る
docker compose exec ollama bash
# docker compose exec open-webui bash

# モデルを作成する
ollama run llama3
# ollama run gemma
# ollama run llava

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
http://localhost:3000/  
```bash
ID: admin@example.com
パスワード dU3inxfX
```

2. モデルを設定する

```bash
docker compose exec open-webui bash

```

# モデルの動作確認
```bash
docker compose logs ollama

curl http://localhost:11434/api/chat -d '{
  "model": "llama3",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
  "stream": false
}'

```

## 参考

ローカルLLMの使用 - OllamaとOpen WebUIの連携について解説  
https://qiita.com/RyutoYoda/items/ecdfbef8c73aae64aa45

Apple Silicon(M3) Macで Ollama を動かしてみた  
https://zenn.dev/mori2_jp/articles/a6b3b4ba17ac01
