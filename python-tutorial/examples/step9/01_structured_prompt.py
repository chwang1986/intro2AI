#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
结构化 Prompt 构建演示

本脚本展示如何构建结构化的 Prompt，通过函数将角色、任务、约束等要素组合成清晰的指令。
可以直接运行：python3 01_structured_prompt.py
"""


def build_prompt(role: str, task: str, constraints: str = "") -> str:
    """
    构建结构化的 Prompt 字符串。

    参数:
        role: AI 的角色设定，例如"专业翻译"、"技术文档撰写者"
        task: 具体任务描述
        constraints: 额外约束条件（可选），例如格式要求、字数限制等

    返回:
        格式化后的完整 Prompt 字符串
    """
    prompt_lines = [
        f"【角色】{role}",
        f"【任务】{task}",
    ]
    if constraints:
        prompt_lines.append(f"【约束】{constraints}")
    prompt_lines.append("【输出】")

    return "\n".join(prompt_lines)


def demo_translation():
    """演示：翻译场景的结构化 Prompt。"""
    print("=" * 50)
    print("场景一：翻译")
    print("=" * 50)

    prompt = build_prompt(
        role="资深中英翻译专家，精通技术文档翻译",
        task="将以下英文技术文档翻译成中文，保持专业术语准确。",
        constraints="1. 保留所有专有名词的英文原词\n2. 输出格式：先原文，后译文"
    )

    print("\n生成的 Prompt：")
    print("-" * 40)
    print(prompt)
    print("-" * 40)
    print("示例输入：Python is a high-level programming language.")
    print()


def demo_summarization():
    """演示：总结场景的结构化 Prompt。"""
    print("=" * 50)
    print("场景二：总结")
    print("=" * 50)

    prompt = build_prompt(
        role="专业内容编辑，擅长提炼关键信息",
        task="阅读以下文章，生成一段简洁的摘要。",
        constraints="1. 摘要字数控制在 100 字以内\n2. 包含文章的核心观点和结论\n3. 使用第三人称"
    )

    print("\n生成的 Prompt：")
    print("-" * 40)
    print(prompt)
    print("-" * 40)
    print("示例输入：[一篇关于人工智能发展的长文章...]")
    print()


def demo_code_generation():
    """演示：代码生成场景的结构化 Prompt。"""
    print("=" * 50)
    print("场景三：代码生成")
    print("=" * 50)

    prompt = build_prompt(
        role="资深 Python 开发工程师，代码规范、注释清晰",
        task="根据需求编写一个 Python 函数。",
        constraints=(
            "1. 使用类型注解\n"
            "2. 包含文档字符串（docstring）\n"
            "3. 添加异常处理\n"
            "4. 提供至少 2 个使用示例"
        )
    )

    print("\n生成的 Prompt：")
    print("-" * 40)
    print(prompt)
    print("-" * 40)
    print("示例输入：写一个函数，计算斐波那契数列的第 n 项。")
    print()


def demo_custom():
    """演示：自定义场景，展示如何灵活组合参数。"""
    print("=" * 50)
    print("场景四：自定义（无约束）")
    print("=" * 50)

    # 不传 constraints，展示可选参数的灵活性
    prompt = build_prompt(
        role="创意写作助手",
        task="根据给定的开头续写一个短篇故事。"
    )

    print("\n生成的 Prompt：")
    print("-" * 40)
    print(prompt)
    print("-" * 40)
    print("示例输入：深夜的图书馆里，一本从未见过的书自动翻开了...")
    print()


def main():
    """主函数：运行所有 Prompt 构建示例。"""
    print("\n结构化 Prompt 构建演示\n")
    print("每个场景展示不同角色、任务和约束的组合方式。\n")

    demo_translation()
    demo_summarization()
    demo_code_generation()
    demo_custom()

    print("=" * 50)
    print("总结")
    print("=" * 50)
    print("结构化 Prompt 的核心要素：")
    print("1. 角色（Role）：定义 AI 的身份和专业领域")
    print("2. 任务（Task）：明确具体要做的事情")
    print("3. 约束（Constraints）：规定输出格式、风格等要求")
    print("=" * 50)


if __name__ == "__main__":
    main()
