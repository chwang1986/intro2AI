#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02_calculator.py
本脚本展示 Python 的基本算术运算：
- 加、减、乘、除
- 整除、取余、幂运算
"""

# 定义两个数字
a = 17
b = 5

print(f"两个数字：a = {a}，b = {b}")
print("-" * 30)

# 加法
print(f"加法：        {a} + {b} = {a + b}")

# 减法
print(f"减法：        {a} - {b} = {a - b}")

# 乘法
print(f"乘法：        {a} * {b} = {a * b}")

# 除法（结果是浮点数）
print(f"除法：        {a} / {b} = {a / b}")

# 整除（向下取整）
print(f"整除：        {a} // {b} = {a // b}")

# 取余（模运算）
print(f"取余：        {a} % {b} = {a % b}")

# 幂运算
print(f"幂运算：      {a} ** {b} = {a ** b}")

print("-" * 30)
print("复合运算示例：")
print(f"(a + b) * 2 = {(a + b) * 2}")
print(f"a + b * 2   = {a + b * 2}  （注意运算优先级！）")
