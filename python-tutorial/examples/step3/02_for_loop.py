#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02_for_loop.py
本脚本展示 for 循环的用法：
- 遍历列表打印每个元素
- range() 的用法
- enumerate() 获取索引和值
"""

# 1. 遍历列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("=== 遍历列表 ===")
for fruit in fruits:
    print(f"  水果：{fruit}")

print("-" * 30)

# 2. 遍历字符串
word = "Python"
print("=== 遍历字符串 ===")
for char in word:
    print(f"  字符：{char}")

print("-" * 30)

# 3. range() 的用法
print("=== range() 用法 ===")
print("range(5):")
for i in range(5):
    print(f"  {i}")

print("\nrange(2, 6):")
for i in range(2, 6):
    print(f"  {i}")

print("\nrange(0, 10, 2):  # 步长为 2")
for i in range(0, 10, 2):
    print(f"  {i}")

print("-" * 30)

# 4. enumerate() 获取索引和值
print("=== enumerate() 用法 ===")
colors = ["红色", "绿色", "蓝色"]
for index, color in enumerate(colors):
    print(f"  索引 {index}：{color}")

print("\n从 1 开始计数：")
for index, color in enumerate(colors, start=1):
    print(f"  第 {index} 个：{color}")

print("-" * 30)

# 5. 计算列表总和
numbers = [10, 20, 30, 40, 50]
total = 0
for n in numbers:
    total += n
print(f"数字列表：{numbers}")
print(f"总和：{total}")
