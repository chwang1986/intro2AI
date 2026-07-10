#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_while_loop.py
本脚本展示 while 循环的用法：
- 简单的计数器
- 用户输入密码直到正确
- break 和 continue 的用法
"""

# 1. 简单的计数器
print("=== 计数器 ===")
count = 1
while count <= 5:
    print(f"  当前计数：{count}")
    count += 1
print("计数结束")

print("-" * 30)

# 2. break：跳出循环
print("=== break 示例 ===")
n = 1
while True:
    if n > 5:
        print("n 大于 5，跳出循环")
        break
    print(f"  n = {n}")
    n += 1

print("-" * 30)

# 3. continue：跳过当前迭代
print("=== continue 示例 ===")
i = 0
while i < 6:
    i += 1
    if i == 3:
        print("  跳过 3")
        continue
    print(f"  i = {i}")

print("-" * 30)

# 4. 用户输入密码直到正确
print("=== 密码验证 ===")
correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input(f"请输入密码（还剩 {max_attempts - attempts} 次机会）：")
    attempts += 1
    if user_input == correct_password:
        print("密码正确，欢迎！")
        break
    else:
        print("密码错误！")
else:
    # while 的 else 子句：循环正常结束（未遇到 break）时执行
    print("次数用尽，账户已锁定")
