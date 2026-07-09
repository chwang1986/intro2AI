#!/bin/bash
# 推送 Intro2AI 项目到 GitHub

cd "$(dirname "$0")"

echo "📦 正在推送到 GitHub..."
echo ""

git add .
git commit -m "update: $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main

echo ""
echo "✅ 推送完成"
echo "   仓库地址: https://github.com/chwang1986/intro2AI"
