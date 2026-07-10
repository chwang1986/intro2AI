#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ollama 调用教程
理解大模型接口、基本原理与高级用法
"""

from flask import Flask, render_template
import os
import jinja2

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 模板搜索路径：子项目 templates + 根目录 design-system
app.jinja_loader = jinja2.FileSystemLoader([
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, '..', 'design-system'),
])

STEPS = [
    {"id": "step1", "title": "大模型基本原理", "desc": "Transformer、注意力机制、Token 与参数规模"},
    {"id": "step2", "title": "Ollama 部署与接口", "desc": "本地安装、REST API 结构、模型管理"},
    {"id": "step3", "title": "基础调用方式", "desc": "Python requests / ollama 库、生成与聊天"},
    {"id": "step4", "title": "高级用法", "desc": "流式输出、系统提示、温度参数、多轮对话"},
    {"id": "step5", "title": "实际应用", "desc": "文本生成、代码辅助、结构化输出 / JSON Mode"},
]


@app.route("/")
def index():
    return render_template("index.html", steps=STEPS)


@app.route("/step<int:num>")
def step(num):
    if 1 <= num <= 5:
        return render_template(f"step{num}.html", steps=STEPS, current_step=num)
    return "Not Found", 404


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=5006)
    args = parser.parse_args()

    print(f"\n🌐 服务器启动: http://{args.host}:{args.port}")
    if args.host == "0.0.0.0":
        import socket
        try:
            local_ip = socket.getaddrinfo(socket.gethostname(), None)[0][4][0]
            print(f"   局域网访问: http://{local_ip}:{args.port}")
        except:
            pass

    app.run(host=args.host, port=args.port, debug=True)
