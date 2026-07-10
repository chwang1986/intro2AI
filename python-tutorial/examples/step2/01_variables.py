#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_variables.py
本脚本展示变量的基本用法：
- 变量赋值（整数、浮点数、字符串、布尔值）
- 使用 type() 查看数据类型
- 变量的重新赋值（动态类型）
"""

# 1. 整数
age = 25
print(f"年龄：{age}，类型：{type(age)}")

# 2. 浮点数
height = 1.75
print(f"身高：{height}，类型：{type(height)}")

# 3. 字符串
name = "小明"
print(f"姓名：{name}，类型：{type(name)}")

# 4. 布尔值
is_student = True
print(f"是否学生：{is_student}，类型：{type(is_student)}")

print("-" * 30)

# 5. 动态类型：变量可以重新赋值为不同类型
x = 100
print(f"x = {x}，类型：{type(x)}")

x = "一百"
print(f"x = {x}，类型：{type(x)}")

x = 3.14
print(f"x = {x}，类型：{type(x)}")

x = False
print(f"x = {x}，类型：{type(x)}")

print("-" * 30)
print("变量可以同时赋值多个值：")
a, b, c = 1, 2.5, "hello"
print(f"a = {a}, b = {b}, c = {c}")
