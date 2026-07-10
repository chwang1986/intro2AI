#!/bin/bash
# 无线电能输电教程启动脚本

cd "$(dirname "$0")"

# 激活虚拟环境
if [ -d "../venv/" ]; then
    source ../venv/bin/activate
fi

PORT=${1:-5005}
HOST=${2:-0.0.0.0}

IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | head -1 | awk '{print $2}')

echo "⚡ 启动无线电能输电教程..."
echo "   本地访问: http://localhost:$PORT"
echo "   局域网访问: http://${IP}:$PORT"
echo ""

python3 app.py --host "$HOST" --port "$PORT"
