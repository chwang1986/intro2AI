#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Few-shot Prompt 演示

本脚本展示 Few-shot Prompting（少样本提示）技术：
通过给 AI 提供几个示例，让它学习某种模式，然后按同样的模式处理新问题。

示例任务：情感分析（判断文本是正面还是负面）
可以直接运行：python3 02_few_shot.py
"""


def build_few_shot_prompt(new_text: str) -> str:
    """
    构建一个 Few-shot Prompt，用于情感分析任务。

    参数:
        new_text: 需要分析情感的新文本

    返回:
        包含示例和待分析文本的完整 Prompt 字符串
    """
    # 正面示例（3 个）
    positive_examples = [
        ("这部电影太精彩了，剧情引人入胜！", "正面"),
        ("服务员态度非常好，用餐体验很棒。", "正面"),
        ("产品质量超出预期，性价比很高。", "正面"),
    ]

    # 负面示例（3 个）
    negative_examples = [
        ("物流太慢了，等了一周才收到货。", "负面"),
        ("客服态度很差，问题一直没有解决。", "负面"),
        ("这个软件经常闪退，体验非常糟糕。", "负面"),
    ]

    lines = [
        "【任务】判断以下文本的情感倾向，只输出"正面"或"负面"。",
        "",
        "【示例】",
    ]

    # 添加正面示例
    for text, label in positive_examples:
        lines.append(f"文本：{text}")
        lines.append(f"情感：{label}")
        lines.append("")

    # 添加负面示例
    for text, label in negative_examples:
        lines.append(f"文本：{text}")
        lines.append(f"情感：{label}")
        lines.append("")

    # 添加待分析的文本
    lines.append("【待分析】")
    lines.append(f"文本：{new_text}")
    lines.append("情感：")

    return "\n".join(lines)


def main():
    """主函数：展示 Few-shot Prompt 的效果。"""
    print("=" * 50)
    print("Few-shot Prompt 演示：情感分析")
    print("=" * 50)
    print()
    print("原理：给 AI 提供几个带标签的示例，让它学会判断规则，")
    print("      然后按同样的模式分析新的文本。")
    print()

    # 测试几条不同的文本
    test_texts = [
        "今天天气真好，心情也跟着明朗起来了！",
        "排队排了两个小时，太让人失望了。",
        "这家咖啡店的拿铁味道一般般。"
    ]

    for i, text in enumerate(test_texts, 1):
        print(f"--- 测试 {i} ---")
        print(f"待分析文本: {text}")
        print()

        prompt = build_few_shot_prompt(text)
        print("生成的完整 Prompt：")
        print("-" * 40)
        print(prompt)
        print("-" * 40)
        print()

    print("=" * 50)
    print("Few-shot Prompt 的关键点：")
    print("1. 示例要覆盖不同类别（正面 / 负面）")
    print("2. 示例格式要统一（输入 → 输出）")
    print("3. 示例数量适中（通常 3~5 个效果较好）")
    print("4. 新问题的格式要与示例一致")
    print("=" * 50)


if __name__ == "__main__":
    main()
