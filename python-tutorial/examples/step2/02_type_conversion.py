#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02_type_conversion.py
本脚本展示 Python 的数据类型转换：
- int()、float()、str()、bool() 的用法
- 字符串与数字的拼接（需要先转换）
"""

# 1. int()：转换为整数
print("=== int() 转换 ===")
print(f"int(3.14)   = {int(3.14)}")      # 浮点转整数，小数部分丢弃
print(f"int('100')  = {int('100')}")     # 字符串转整数
print(f"int(True)   = {int(True)}")      # 布尔转整数
print(f"int(False)  = {int(False)}")

# 2. float()：转换为浮点数
print("\n=== float() 转换 ===")
print(f"float(5)      = {float(5)}")         # 整数转浮点
print(f"float('3.14') = {float('3.14')}")    # 字符串转浮点

# 3. str()：转换为字符串
print("\n=== str() 转换 ===")
print(f"str(100)    = {str(100)}")
print(f"str(3.14)   = {str(3.14)}")
print(f"str(True)   = {str(True)}")

# 4. bool()：转换为布尔值
print("\n=== bool() 转换 ===")
print(f"bool(1)     = {bool(1)}")      # 非零数为 True
print(f"bool(0)     = {bool(0)}")      # 零为 False
print(f"bool('')    = {bool('')}")     # 空字符串为 False
print(f"bool('hi')  = {bool('hi')}")   # 非空字符串为 True

print("-" * 30)

# 5. 字符串和数字的拼接需要先转换
year = 2024
# 下面这行会报错，不能直接拼接字符串和数字：
# message = "今年是" + year + "年"

# 正确做法：用 str() 转换
message = "今年是" + str(year) + "年"
print(message)

# 更推荐的方式：使用 f-string（不需要手动转换）
message2 = f"今年是{year}年"
print(message2)

# 从用户输入获取数字（input 返回的是字符串，需要转换）
# user_input = input("请输入一个数字：")
# number = int(user_input)
# print(f"你输入的数字加 10 等于：{number + 10}")
