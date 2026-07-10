#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Frontend Design System Tutorial
前端设计系统教程
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

# 阶段列表
STEPS = [
    {"id": "step1", "title": "设计原则", "desc": "对齐、对比、重复、亲密性；大厂设计价值观"},
    {"id": "step2", "title": "色彩系统", "desc": "设计令牌、主色、辅色、功能色、中性色阶"},
    {"id": "step3", "title": "字体系统", "desc": "字体族、字号层级、字重、行高与排版节奏"},
    {"id": "step4", "title": "间距与布局", "desc": "8px网格、留白法则、容器、响应式断点"},
    {"id": "step5", "title": "基础组件", "desc": "按钮、输入框、标签、徽章的规范与变体"},
    {"id": "step6", "title": "容器组件", "desc": "卡片、面板、模态框、导航栏的设计模式"},
    {"id": "step7", "title": "数据展示", "desc": "表格、列表、空状态、加载与进度"},
    {"id": "step8", "title": "响应式设计", "desc": "移动端适配、弹性布局、断点策略"},
    {"id": "step9", "title": "动画与交互", "desc": "过渡曲线、状态反馈、微交互原则"},
    {"id": "step10", "title": "页面模板", "desc": "可直接套用的页面结构与实战组合"},
]


@app.route("/")
def index():
    return render_template("index.html", steps=STEPS)


@app.route("/step<int:num>")
def step(num):
    if 1 <= num <= 10:
        return render_template(f"step{num}.html", steps=STEPS, current_step=num)
    return "Not Found", 404


@app.route("/practice")
def practice():
    return render_template("practice.html", steps=STEPS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=True)
