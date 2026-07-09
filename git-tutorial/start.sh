#!/bin/bash
# 启动 git-tutorial 教程服务

cd "$(dirname "$0")"

# 激活虚拟环境（使用 intro2AI 项目共享的虚拟环境）
if [ -d "../本地ollama模型调用/venv/" ]; then
    source ../本地ollama模型调用/venv/bin/activate
elif [ -d "../../本地ollama模型调用/venv/" ]; then
    source ../../本地ollama模型调用/venv/bin/activate
fi

# 获取本机 IP
IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | head -1 | awk '{print $2}')

echo "🚀 启动 Git 教程服务..."
echo "   本地访问: http://localhost:5002"
echo "   局域网访问: http://${IP}:5002"
echo ""

python3 app.py --host=0.0.0.0 --port=5002
