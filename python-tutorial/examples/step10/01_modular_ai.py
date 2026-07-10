#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模块化 AI 开发演示

本脚本展示如何将一个大任务拆分成多个小模块，每个模块负责一个子任务。
通过 mock 数据模拟 AI 生成，演示模块化设计的思路和好处。

模块划分：
- generate_title()    : 生成文章标题
- generate_outline()  : 生成文章大纲
- generate_content()  : 根据大纲生成正文
- main()             : 组装所有模块，输出完整文章

可以直接运行：python3 01_modular_ai.py
"""

import random


def generate_title(topic: str) -> str:
    """
    模块一：根据主题生成文章标题。

    参数:
        topic: 文章主题

    返回:
        AI 生成的标题字符串
    """
    # Mock：模拟 AI 返回的标题（实际应用中调用 API）
    mock_titles = [
        f"深入理解{topic}：从入门到精通",
        f"{topic}完全指南：新手必读",
        f"探索{topic}的奥秘与实践",
        f"一文读懂{topic}",
    ]
    title = random.choice(mock_titles)
    print(f"[模块: 生成标题] -> {title}")
    return title


def generate_outline(topic: str) -> list:
    """
    模块二：根据主题生成文章大纲。

    参数:
        topic: 文章主题

    返回:
        大纲条目列表，每个条目是一个字典
    """
    # Mock：模拟 AI 返回的结构化大纲
    mock_outlines = {
        "人工智能": [
            {"section": "一、什么是人工智能", "points": ["定义与历史", "主要分支领域"]},
            {"section": "二、核心技术", "points": ["机器学习", "深度学习", "自然语言处理"]},
            {"section": "三、应用场景", "points": ["医疗诊断", "自动驾驶", "智能客服"]},
            {"section": "四、未来展望", "points": ["发展趋势", "伦理挑战"]},
        ],
        "Python 编程": [
            {"section": "一、Python 简介", "points": ["语言特点", "应用领域"]},
            {"section": "二、基础语法", "points": ["变量与数据类型", "控制流程", "函数定义"]},
            {"section": "三、进阶特性", "points": ["面向对象编程", "装饰器", "生成器"]},
            {"section": "四、实战项目", "points": ["Web 开发", "数据分析", "自动化脚本"]},
        ],
    }

    # 如果主题匹配，返回预设大纲；否则返回通用大纲
    outline = mock_outlines.get(topic, [
        {"section": f"一、{topic}概述", "points": ["基本概念", "发展背景"]},
        {"section": f"二、{topic}的核心要素", "points": ["关键组成部分", "工作原理"]},
        {"section": f"三、{topic}的应用", "points": ["实际案例", "行业影响"]},
        {"section": f"四、总结与展望", "points": ["主要结论", "未来方向"]},
    ])

    print(f"[模块: 生成大纲] -> 共 {len(outline)} 个章节")
    for item in outline:
        print(f"    - {item['section']}")
    return outline


def generate_content(section: dict, topic: str) -> str:
    """
    模块三：根据大纲条目生成正文内容。

    参数:
        section: 大纲条目字典，包含 section 和 points
        topic: 文章主题

    返回:
        该章节的正文内容
    """
    section_title = section["section"]
    points = section["points"]

    # Mock：模拟 AI 根据大纲生成内容
    lines = [f"\n{section_title}"]
    lines.append("=" * 40)

    for point in points:
        lines.append(f"\n▶ {point}")
        lines.append(f"  这里是关于「{point}」的详细内容。")
        lines.append(f"  在实际应用中，AI 会根据「{topic}」这一主题，")
        lines.append(f"  围绕「{point}」生成专业、连贯的段落文字。")

    content = "\n".join(lines)
    print(f"[模块: 生成内容] -> {section_title} (包含 {len(points)} 个要点)")
    return content


def assemble_article(title: str, outline: list, contents: list) -> str:
    """
    组装模块：将标题、大纲和各章节内容组装成完整文章。

    参数:
        title: 文章标题
        outline: 大纲列表
        contents: 各章节内容列表

    返回:
        完整文章字符串
    """
    article_lines = [
        "=" * 50,
        f"题目：{title}",
        "=" * 50,
        "\n【文章大纲】",
    ]

    for item in outline:
        article_lines.append(f"  {item['section']}")
        for point in item["points"]:
            article_lines.append(f"    - {point}")

    article_lines.append("\n" + "=" * 50)
    article_lines.append("【正文内容】")
    article_lines.append("=" * 50)

    for content in contents:
        article_lines.append(content)

    article_lines.append("\n" + "=" * 50)
    article_lines.append("【文章结束】")
    article_lines.append("=" * 50)

    return "\n".join(article_lines)


def main():
    """
    主函数：演示模块化开发流程。

    步骤：
        1. 确定主题
        2. 调用 generate_title() 生成标题
        3. 调用 generate_outline() 生成大纲
        4. 遍历大纲，调用 generate_content() 逐章生成内容
        5. 调用 assemble_article() 组装完整文章
    """
    print("=" * 50)
    print("模块化 AI 文章生成演示")
    print("=" * 50)
    print()

    # 步骤 1：确定主题
    topic = "人工智能"
    print(f"输入主题: {topic}\n")

    # 步骤 2：生成标题
    title = generate_title(topic)
    print()

    # 步骤 3：生成大纲
    outline = generate_outline(topic)
    print()

    # 步骤 4：逐章生成内容
    contents = []
    for section in outline:
        content = generate_content(section, topic)
        contents.append(content)
    print()

    # 步骤 5：组装文章
    print("[模块: 组装文章] -> 合并所有内容...")
    article = assemble_article(title, outline, contents)

    # 输出最终结果
    print("\n" + "=" * 50)
    print("最终输出")
    print("=" * 50)
    print(article)

    print("\n" + "=" * 50)
    print("模块化设计的好处：")
    print("1. 每个模块职责单一，易于理解和维护")
    print("2. 可以单独测试和优化每个模块")
    print("3. 便于复用，比如 generate_title() 可用于其他场景")
    print("4. 主函数逻辑清晰，像搭积木一样组合功能")
    print("=" * 50)


if __name__ == "__main__":
    main()
