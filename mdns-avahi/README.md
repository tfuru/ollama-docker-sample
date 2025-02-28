# ollama コンテナー

```
# ollama コンテナに入る
docker compose exec mdns-avahi bash

# /etc/init.d/dbus start
# /etc/init.d/avahi-daemon start
# /etc/init.d/avahi-daemon status
# /etc/init.d/avahi-daemon restart

# ping -c 5 llm-server.local

```

# ホストで確認

```
ping -c 5 llm-server.local

curl -v http://llm-server.local:11434
```
