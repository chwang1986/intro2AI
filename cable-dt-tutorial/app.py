from flask import Flask, render_template
import jinja2

app = Flask(__name__)
app.jinja_loader = jinja2.FileSystemLoader([
    'cable-dt-tutorial/templates',
    'design-system'
])

steps = [
    {"num": "01", "id": "step1", "title": "研究背景与意义", "desc": "为什么用数据驱动电缆质量分析，这个方向的价值在哪里"},
    {"num": "02", "id": "step2", "title": "相关领域概述", "desc": "数据治理、数字孪生、平行系统、工业大数据的概念与关系"},
    {"num": "03", "id": "step3", "title": "研究思路与技术路线", "desc": "从整体架构到具体步骤，梳理研究工作的完整路径"},
    {"num": "04", "id": "step4", "title": "数据处理方法", "desc": "数据清洗、特征工程、时序分析、异常检测、质量预测模型"},
    {"num": "05", "id": "step5", "title": "论文发表方向", "desc": "可投稿的期刊、会议、选题角度和写作要点"},
    {"num": "06", "id": "step6", "title": "专利申请方向", "desc": "可申请的专利类型、已有专利分析和创新点挖掘"},
    {"num": "07", "id": "step7", "title": "软件系统设计", "desc": "系统架构、技术栈、模块划分和开发思路"},
    {"num": "08", "id": "step8", "title": "实施路线图", "desc": "从0到1的阶段性计划、里程碑和资源配置"},
]

@app.route('/')
def index():
    return render_template('index.html', steps=steps)

@app.route('/<step_id>')
def step(step_id):
    return render_template(f'{step_id}.html', steps=steps)

if __name__ == '__main__':
    app.run(debug=True, port=5007)
