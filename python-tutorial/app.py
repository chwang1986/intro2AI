#!/usr/bin/env python3
"""
python-tutorial —— Python 编程简明教程
面向 AI 时代的开发者学习路径
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


# ============================================================
# 页面路由
# ============================================================

@app.route("/")
def index():
    """教程主页：纲领 + 目标 + 大纲"""
    steps = [
        {"num": "01", "title": "Python 是什么", "desc": "环境搭建与第一个程序", "path": "/step1", "done": True},
        {"num": "02", "title": "变量与类型", "desc": "数字、字符串、布尔值", "path": "/step2", "done": True},
        {"num": "03", "title": "控制流", "desc": "if/else、for、while", "path": "/step3", "done": True},
        {"num": "04", "title": "函数", "desc": "定义、参数、返回值", "path": "/step4", "done": True},
        {"num": "05", "title": "数据结构", "desc": "列表、字典、元组、集合", "path": "/step5", "done": True},
        {"num": "06", "title": "文件与异常", "desc": "读写文件、错误处理", "path": "/step6", "done": True},
        {"num": "07", "title": "面向对象", "desc": "类、对象、继承", "path": "/step7", "done": True},
        {"num": "08", "title": "调用 AI API", "desc": "与 AI 模型交互", "path": "/step8", "done": True},
        {"num": "09", "title": "Prompt 工程", "desc": "设计有效的 AI 指令", "path": "/step9", "done": True},
        {"num": "10", "title": "AI 协作工作流", "desc": "人与 AI 的配合方式", "path": "/step10", "done": True},
        {"num": "11", "title": "综合实战", "desc": "从零写一个实用程序", "path": "/practice", "done": True},
    ]
    return render_template("index.html", steps=steps)


@app.route("/step1")
def step1():
    """Python 是什么"""
    return render_template("step1.html")


@app.route("/step2")
def step2():
    """变量与类型"""
    return render_template("step2.html")


@app.route("/step3")
def step3():
    """控制流"""
    return render_template("step3.html")


@app.route("/step4")
def step4():
    """函数"""
    return render_template("step4.html")


@app.route("/step5")
def step5():
    """数据结构"""
    return render_template("step5.html")


@app.route("/step6")
def step6():
    """文件与异常"""
    return render_template("step6.html")


@app.route("/step7")
def step7():
    """面向对象"""
    return render_template("step7.html")


@app.route("/step8")
def step8():
    """调用 AI API"""
    return render_template("step8.html")


@app.route("/step9")
def step9():
    """Prompt 工程"""
    return render_template("step9.html")


@app.route("/step10")
def step10():
    """AI 协作工作流"""
    return render_template("step10.html")


@app.route("/practice")
def practice():
    """综合实战"""
    return render_template("practice.html")


# ============================================================
# 启动
# ============================================================

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5003)
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
