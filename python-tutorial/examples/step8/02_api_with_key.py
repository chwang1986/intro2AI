#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从环境变量读取 API Key 并调用 API

本脚本展示如何从环境变量安全读取 API Key，并在请求头中携带它。

【运行前准备】
在终端中设置环境变量（仅当前会话有效）：
    export API_KEY=your_actual_api_key_here

或者创建一个 .env 文件（需要安装 python-dotenv）：
    pip install python-dotenv
    然后在 .env 文件中写入：API_KEY=your_actual_api_key_here

可以直接运行（会先检查环境变量是否存在）：python3 02_api_with_key.py
"""

import os
import json


def get_api_key() -> str:
    """
    从环境变量读取 API Key。

    返回:
        API Key 字符串

    异常:
        如果环境变量未设置，抛出 ValueError
    """
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise ValueError(
            "未找到 API_KEY 环境变量！\n"
            "请在运行前执行：export API_KEY=your_api_key_here\n"
            "或者将 API Key 添加到系统的环境变量中。"
        )
    # 安全起见，只打印前 6 位
    print(f"[API Key 已读取] 前缀: {api_key[:6]}...")
    return api_key


def build_request_headers(api_key: str) -> dict:
    """
    构建包含 API Key 的请求头。

    参数:
        api_key: API Key 字符串

    返回:
        HTTP 请求头字典
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "User-Agent": "PythonTutorial/1.0"
    }
    print("[请求头已构建]")
    print(json.dumps(headers, ensure_ascii=False, indent=2))
    return headers


def mock_api_call(headers: dict, question: str) -> dict:
    """
    模拟发送 API 请求（实际应用中应使用 requests 库）。

    参数:
        headers: 包含 API Key 的请求头
        question: 用户问题

    返回:
        模拟的 API 响应字典
    """
    # 模拟请求体
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "你是一个有帮助的助手。"},
            {"role": "user", "content": question}
        ],
        "temperature": 0.7
    }
    print(f"\n[模拟请求体]\n{json.dumps(payload, ensure_ascii=False, indent=2)}")

    # 模拟几种常见的 API 错误情况
    auth_header = headers.get("Authorization", "")
    if "invalid" in auth_header.lower():
        return {
            "error": {
                "code": "invalid_api_key",
                "message": "提供的 API Key 不正确或已过期，请检查后重试。",
                "type": "authentication_error"
            }
        }

    if "quota" in auth_header.lower():
        return {
            "error": {
                "code": "insufficient_quota",
                "message": "账户额度已用完，请充值或升级套餐。",
                "type": "rate_limit_error"
            }
        }

    # 模拟成功响应
    return {
        "id": "chatcmpl-abc123",
        "object": "chat.completion",
        "model": "gpt-4o-mini",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": f"这是对「{question}」的模拟回答。在实际使用中，这里会返回真实的 AI 生成内容。"
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30
        }
    }


def handle_api_response(response: dict) -> str:
    """
    处理 API 响应，区分成功与错误情况。

    参数:
        response: API 返回的字典

    返回:
        处理后的结果字符串
    """
    if "error" in response:
        error = response["error"]
        code = error.get("code", "unknown_error")
        message = error.get("message", "未知错误")
        return f"[API 错误] 错误码: {code}，信息: {message}"

    try:
        answer = response["choices"][0]["message"]["content"]
        tokens = response["usage"]["total_tokens"]
        return f"AI 回答: {answer}\n[Token 消耗] {tokens}"
    except (KeyError, IndexError) as e:
        return f"[解析错误] 响应格式异常: {e}"


def main():
    """主函数：演示完整的 API Key 调用流程。"""
    print("=" * 50)
    print("API Key 调用 API 演示")
    print("=" * 50)

    try:
        # 1. 读取 API Key
        api_key = get_api_key()

        # 2. 构建请求头
        headers = build_request_headers(api_key)

        # 3. 模拟 API 调用
        print("\n--- 测试正常请求 ---")
        response = mock_api_call(headers, "介绍一下机器学习")
        print(handle_api_response(response))

        # 4. 模拟 API Key 错误
        print("\n--- 模拟 API Key 错误 ---")
        bad_headers = build_request_headers("invalid_key_12345")
        response = mock_api_call(bad_headers, "测试问题")
        print(handle_api_response(response))

        # 5. 模拟额度不足
        print("\n--- 模拟额度不足 ---")
        quota_headers = build_request_headers("quota_exceeded_key")
        response = mock_api_call(quota_headers, "测试问题")
        print(handle_api_response(response))

    except ValueError as e:
        print(f"[配置错误] {e}")
    except Exception as e:
        print(f"[未预期异常] {type(e).__name__}: {e}")

    print("\n" + "=" * 50)
    print("演示结束！")
    print("=" * 50)


if __name__ == "__main__":
    main()
