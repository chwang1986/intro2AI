#!/usr/bin/env python3
"""
git-tutorial —— 如何使用 Git
Intro2AI 项目的第一个教程子目录
"""

import os
from flask import Flask, render_template
import jinja2

app = Flask(__name__)

# 模板搜索路径：子项目 templates + 根目录 design-system
app.jinja_loader = jinja2.FileSystemLoader([
    os.path.join(os.path.dirname(__file__), 'templates'),
    os.path.join(os.path.dirname(__file__), '..', 'design-system'),
])


@app.route("/")
def index():
    """教程主页：纲领 + 目标 + 大纲"""
    steps = [
        {"num": "01", "title": "Git 是什么", "desc": "版本控制的基本概念，为什么需要 Git", "done": True},
        {"num": "02", "title": "初始化仓库", "desc": "git init、git status、工作区与暂存区", "done": True},
        {"num": "03", "title": "添加与提交", "desc": "git add、git commit、提交信息规范", "done": False},
        {"num": "04", "title": "查看历史", "desc": "git log、git diff、版本回退", "done": False},
        {"num": "05", "title": "分支管理", "desc": "git branch、git checkout、合并冲突", "done": False},
        {"num": "06", "title": "远程仓库", "desc": "git remote、git push、git pull、git clone", "done": False},
    ]
    return render_template("index.html", steps=steps)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5002)
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
