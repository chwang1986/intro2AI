#!/usr/bin/env python3
"""
git-tutorial —— 如何使用 Git
Intro2AI 项目的第一个教程子目录
支持真实命令执行与多人协作模拟
"""

import os
import subprocess
import shutil
from flask import Flask, render_template, request, jsonify
import jinja2

# 工作区路径
WORKSPACE = os.path.join(os.path.dirname(__file__), 'workspace')

app = Flask(__name__)

# 模板搜索路径：子项目 templates + 根目录 design-system
app.jinja_loader = jinja2.FileSystemLoader([
    os.path.join(os.path.dirname(__file__), 'templates'),
    os.path.join(os.path.dirname(__file__), '..', 'design-system'),
])

# ============================================================
# 工具函数
# ============================================================

def run_cmd(cmd, cwd=WORKSPACE):
    """在指定目录执行命令，返回 (输出, 错误, 返回码)"""
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd,
            capture_output=True, text=True, timeout=10
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", "命令超时", 1
    except Exception as e:
        return "", str(e), 1


def get_repo_status():
    """获取仓库当前状态"""
    stdout, stderr, _ = run_cmd("git status --short")
    branch, _, _ = run_cmd("git branch --show-current")
    log, _, _ = run_cmd("git log --oneline -5")
    return {
        "status": stdout or "工作区干净",
        "branch": branch.strip() or "无分支",
        "log": log or "无提交记录",
        "has_repo": os.path.exists(os.path.join(WORKSPACE, '.git'))
    }


def reset_workspace():
    """重置工作区为初始状态"""
    if os.path.exists(WORKSPACE):
        shutil.rmtree(WORKSPACE)
    os.makedirs(WORKSPACE)
    # 初始化仓库
    run_cmd("git init")
    run_cmd("git config user.email 'learner@example.com'")
    run_cmd("git config user.name '学习者'")
    # 创建初始文件
    with open(os.path.join(WORKSPACE, 'README.md'), 'w') as f:
        f.write("# 我的项目\n\n这是一个演示项目。\n")
    with open(os.path.join(WORKSPACE, 'main.py'), 'w') as f:
        f.write("print('Hello Git')\n")
    return True


# ============================================================
# 页面路由
# ============================================================

@app.route("/")
def index():
    """教程主页：纲领 + 目标 + 大纲"""
    steps = [
        {"num": "01", "title": "Git 是什么", "desc": "版本控制的基本概念", "path": "/step1", "done": True},
        {"num": "02", "title": "初始化仓库", "desc": "git init、工作区与暂存区", "path": "/step2", "done": True},
        {"num": "03", "title": "添加与提交", "desc": "git add、git commit", "path": "/step3", "done": True},
        {"num": "04", "title": "查看历史与回退", "desc": "git log、diff、checkout", "path": "/step4", "done": True},
        {"num": "05", "title": "分支管理", "desc": "branch、merge、冲突解决", "path": "/step5", "done": True},
        {"num": "06", "title": "远程仓库", "desc": "remote、push、pull、clone", "path": "/step6", "done": True},
        {"num": "07", "title": "多人协作", "desc": "模拟两人协作流程", "path": "/collab", "done": True},
        {"num": "08", "title": "综合实战", "desc": "完整工作流操作", "path": "/practice", "done": True},
    ]
    return render_template("index.html", steps=steps)


@app.route("/step1")
def step1():
    """Git 是什么"""
    return render_template("step1.html")


@app.route("/step2")
def step2():
    """初始化仓库"""
    return render_template("step2.html", status=get_repo_status())


@app.route("/step3")
def step3():
    """添加与提交"""
    return render_template("step3.html", status=get_repo_status())


@app.route("/step4")
def step4():
    """查看历史与回退"""
    return render_template("step4.html", status=get_repo_status())


@app.route("/step5")
def step5():
    """分支管理"""
    return render_template("step5.html", status=get_repo_status())


@app.route("/step6")
def step6():
    """远程仓库"""
    return render_template("step6.html", status=get_repo_status())


@app.route("/collab")
def collab():
    """多人协作模拟"""
    return render_template("collab.html")


@app.route("/practice")
def practice():
    """综合实战"""
    return render_template("practice.html", status=get_repo_status())


# ============================================================
# API 路由
# ============================================================

@app.route("/api/exec", methods=["POST"])
def api_exec():
    """执行 git 命令（安全限制在工作区内）"""
    data = request.get_json() or {}
    cmd = data.get("cmd", "").strip()
    target = data.get("target", "workspace")  # workspace 或 collab_a / collab_b

    if not cmd:
        return jsonify({"error": "命令不能为空"}), 400

    # 安全过滤：只允许 git 相关命令和基础 shell 命令
    allowed_prefixes = ('git ', 'echo ', 'cat ', 'ls', 'touch ', 'mkdir ', 'rm ', 'cp ', 'mv ', 'pwd')
    if not cmd.startswith(allowed_prefixes):
        return jsonify({"error": f"不支持的命令: {cmd}"}), 400

    # 确定工作目录
    if target == "workspace":
        cwd = WORKSPACE
    elif target == "collab_a":
        cwd = os.path.join(os.path.dirname(__file__), 'collab_a')
    elif target == "collab_b":
        cwd = os.path.join(os.path.dirname(__file__), 'collab_b')
    else:
        return jsonify({"error": "无效的目标目录"}), 400

    stdout, stderr, rc = run_cmd(cmd, cwd=cwd)
    return jsonify({
        "cmd": cmd,
        "stdout": stdout,
        "stderr": stderr,
        "code": rc
    })


@app.route("/api/status")
def api_status():
    """获取仓库状态"""
    target = request.args.get("target", "workspace")
    if target == "workspace":
        cwd = WORKSPACE
    elif target == "collab_a":
        cwd = os.path.join(os.path.dirname(__file__), 'collab_a')
    elif target == "collab_b":
        cwd = os.path.join(os.path.dirname(__file__), 'collab_b')
    else:
        return jsonify({"error": "无效目标"}), 400

    if not os.path.exists(os.path.join(cwd, '.git')):
        return jsonify({"status": "未初始化", "branch": "-", "log": "", "files": []})

    stdout, _, _ = run_cmd("git status --short", cwd)
    branch, _, _ = run_cmd("git branch --show-current", cwd)
    log, _, _ = run_cmd("git log --oneline -10", cwd)

    # 获取文件列表
    files = []
    if os.path.exists(cwd):
        for item in sorted(os.listdir(cwd)):
            if item.startswith('.'):
                continue
            path = os.path.join(cwd, item)
            files.append({"name": item, "type": "dir" if os.path.isdir(path) else "file"})

    return jsonify({
        "status": stdout or "工作区干净",
        "branch": branch.strip() or "无分支",
        "log": log or "无提交记录",
        "files": files
    })


@app.route("/api/reset", methods=["POST"])
def api_reset():
    """重置工作区"""
    reset_workspace()
    return jsonify({"message": "工作区已重置"})


@app.route("/api/collab/setup", methods=["POST"])
def api_collab_setup():
    """设置多人协作环境"""
    base = os.path.dirname(__file__)
    collab_a = os.path.join(base, 'collab_a')
    collab_b = os.path.join(base, 'collab_b')
    remote = os.path.join(base, 'remote_repo.git')

    # 清理旧目录
    for d in [collab_a, collab_b, remote]:
        if os.path.exists(d):
            shutil.rmtree(d)

    # 创建裸仓库（模拟远程）
    os.makedirs(remote)
    run_cmd("git init --bare", cwd=remote)

    # 用户 A 克隆并提交
    run_cmd(f"git clone {remote} {collab_a}", cwd=base)
    run_cmd("git config user.email 'userA@example.com'", cwd=collab_a)
    run_cmd("git config user.name '用户A'", cwd=collab_a)
    with open(os.path.join(collab_a, 'README.md'), 'w') as f:
        f.write("# 协作项目\n\n由用户A创建\n")
    run_cmd("git add .", cwd=collab_a)
    run_cmd("git commit -m '用户A: 初始化项目'", cwd=collab_a)
    run_cmd("git push origin main", cwd=collab_a)

    # 用户 B 克隆
    run_cmd(f"git clone {remote} {collab_b}", cwd=base)
    run_cmd("git config user.email 'userB@example.com'", cwd=collab_b)
    run_cmd("git config user.name '用户B'", cwd=collab_b)

    return jsonify({"message": "协作环境已创建"})


# ============================================================
# 启动
# ============================================================

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
