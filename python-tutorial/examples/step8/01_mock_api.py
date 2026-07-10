#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模拟调用 AI API（Mock 版本）

本脚本展示如何模拟调用 AI API，不依赖真实的 API Key。
通过本地预设的 mock 数据，演示请求构造、JSON 响应解析和错误处理。
可以直接运行：python3 01_mock_api.py
"""

import json
import random
import time


def ask_ai(question: str) -> dict:
    """
    模拟调用 AI API，返回预设的 mock 回答。

    参数:
        question: 用户输入的问题

    返回:
        包含 status、answer、tokens 等字段的字典，模拟真实 API 响应结构
    """
    # 模拟网络延迟（100~500 毫秒）
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)

    # 模拟网络异常（10% 概率）
    if random.random() < 0.1:
        raise ConnectionError("模拟网络错误：无法连接到 AI 服务器，请检查网络后重试。")

    # 模拟超时（5% 概率）
    if random.random() < 0.05:
        raise TimeoutError("模拟超时错误：AI 服务器响应时间过长，请稍后重试。")

    # 模拟请求体结构（展示真实场景中通常会构造的 JSON）
    request_body = {
        "model": "mock-gpt-4o",
        "messages": [
            {"role": "system", "content": "你是一个有帮助的 AI 助手。"},
            {"role": "user", "content": question}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }
    print(f"[模拟请求体] {json.dumps(request_body, ensure_ascii=False, indent=2)}")

    # 预设的 mock 回答库
    mock_answers = {
        "你好": "你好！很高兴见到你，有什么我可以帮你的吗？",
        "python": "Python 是一种简洁优雅的编程语言，非常适合人工智能开发。",
        "ai": "人工智能（AI）是让计算机模拟人类智能的技术领域，包括机器学习、深度学习等。",
        "api": "API（应用程序接口）是不同软件系统之间通信的桥梁，通过 HTTP 请求交换数据。",
    }

    # 根据关键词匹配回答，否则返回通用回答
    answer = "这是一个通用的模拟回答。在实际应用中，这里会返回 AI 模型生成的内容。"
    for key, value in mock_answers.items():
        if key.lower() in question.lower():
            answer = value
            break

    # 模拟 JSON 响应结构
    response = {
        "status": "success",
        "data": {
            "id": "mock-req-" + str(random.randint(10000, 99999)),
            "model": "mock-gpt-4o",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": answer
                    },
                    "finish_reason": "stop"
                }
            ],
            "usage": {
                "prompt_tokens": len(question),
                "completion_tokens": len(answer),
                "total_tokens": len(question) + len(answer)
            }
        }
    }

    return response


def parse_response(response: dict) -> str:
    """
    解析模拟 API 响应，提取 AI 回答内容。

    参数:
        response: ask_ai 返回的响应字典

    返回:
        AI 生成的文本内容
    """
    try:
        if response.get("status") != "success":
            return f"请求失败：{response.get('message', '未知错误')}"

        answer = response["data"]["choices"][0]["message"]["content"]
        tokens = response["data"]["usage"]["total_tokens"]
        print(f"[Token 消耗] 总共使用了 {tokens} 个 token")
        return answer
    except (KeyError, IndexError) as e:
        return f"解析响应失败：{e}"


def main():
    """主函数：演示模拟 API 调用流程。"""
    print("=" * 50)
    print("模拟 AI API 调用演示")
    print("=" * 50)

    # 测试问题列表
    questions = [
        "你好",
        "什么是 Python？",
        "给我介绍一下 AI",
        "API 是什么？",
        "这是一个测试问题"
    ]

    for q in questions:
        print(f"\n用户问题: {q}")
        print("-" * 40)
        try:
            response = ask_ai(q)
            answer = parse_response(response)
            print(f"AI 回答: {answer}")
        except ConnectionError as e:
            print(f"[网络异常] {e}")
        except TimeoutError as e:
            print(f"[超时异常] {e}")
        except Exception as e:
            print(f"[未知异常] {e}")

    print("\n" + "=" * 50)
    print("演示结束！")
    print("=" * 50)


if __name__ == "__main__":
    main()
