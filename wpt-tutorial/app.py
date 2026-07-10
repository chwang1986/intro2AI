#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wireless Power Transfer Tutorial
无线电能输电教程
"""

from flask import Flask, render_template
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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


@app.route("/step<int:num>.html")
def step(num):
    if 1 <= num <= 5:
        return render_template(f"step{num}.html", steps=STEPS, current_step=num)
    return "Not Found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
