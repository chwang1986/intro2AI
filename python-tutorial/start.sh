#!/bin/bash
# Python 教程启动脚本

cd "$(dirname "$0")"

PORT=${1:-5003}
HOST=${2:-127.0.0.1}

echo "🐍 启动 Python 教程..."
echo "   本地访问: http://$HOST:$PORT"

if [ "$HOST" = "0.0.0.0" ]; then
    LOCAL_IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | head -1 | awk '{print $2}')
    echo "   局域网访问: http://$LOCAL_IP:$PORT"
fi

echo ""
python3 app.py --host "$HOST" --port "$PORT"
