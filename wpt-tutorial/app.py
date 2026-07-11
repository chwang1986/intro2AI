#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wireless Power Transfer Tutorial
无线电能输电教程
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
    {"id": "step1", "title": "什么是无线输电", "desc": "概念、历史、分类与基本原理"},
    {"id": "step2", "title": "电磁感应与互感", "desc": "法拉第定律、变压器模型、互感系数"},
    {"id": "step3", "title": "磁共振耦合", "desc": "LC谐振、耦合系数、频率分裂现象"},
    {"id": "step4", "title": "效率推导", "desc": "等效电路、阻抗匹配、最大效率条件"},
    {"id": "step5", "title": "应用与挑战", "desc": "手机充电、电动汽车、医疗植入、空间太阳能"},
]


@app.route("/")
def index():
    return render_template("index.html", steps=STEPS)


@app.route("/<step_id>")
def step(step_id):
    for i, s in enumerate(STEPS, 1):
        if s["id"] == step_id:
            return render_template(f"{step_id}.html", steps=STEPS, current_step=i)
    return "Not Found", 404


@app.route('/appendix')
def appendix():
    return render_template('appendix.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
