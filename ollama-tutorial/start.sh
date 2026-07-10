#!/bin/bash
# ============================================
# 本地启动脚本 — Ollama 调用教程
# 用法: bash start.sh
# ============================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 使用共享虚拟环境
VENV="../venv/bin/python"
if [ ! -f "$VENV" ]; then
    echo "❌ 错误: 未找到共享虚拟环境 ../venv"
    echo "   请在 intro2AI 目录下运行: python3 -m venv venv && venv/bin/pip install flask"
    exit 1
fi

PORT=5006
while lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; do
    PORT=$((PORT + 1))
    if [ $PORT -gt 5010 ]; then
        echo "❌ 错误: 5006-5010 端口均被占用"
        exit 1
    fi
done

echo "🚀 启动 Ollama 调用教程..."
echo "🔗 访问地址: http://localhost:$PORT"
echo "🛑 按 Ctrl+C 停止服务器"
echo ""

unset PYTHONHOME
unset PYTHONPATH
exec "$VENV" app.py --port $PORT
