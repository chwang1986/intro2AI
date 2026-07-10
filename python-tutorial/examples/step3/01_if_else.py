#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_if_else.py
本脚本展示条件判断的用法：
- 判断年龄是否成年
- 判断数字正负零
- 多条件判断（elif）
"""

# 1. 判断年龄是否成年
age = 20
print(f"年龄：{age}")
if age >= 18:
    print("已成年")
else:
    print("未成年")

print("-" * 30)

# 2. 判断数字正负零
num = -7
print(f"数字：{num}")
if num > 0:
    print("这是一个正数")
elif num < 0:
    print("这是一个负数")
else:
    print("这是零")

print("-" * 30)

# 3. 多条件判断：成绩等级
score = 85
print(f"成绩：{score}")
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"
print(f"等级：{grade}")

print("-" * 30)

# 4. 多个条件的组合
temperature = 28
is_raining = False
print(f"气温：{temperature}°C，是否下雨：{is_raining}")
if temperature > 30 and not is_raining:
    print("天气炎热，注意防晒")
elif temperature > 20 and not is_raining:
    print("天气不错，适合出行")
else:
    print("天气不佳，建议带伞")
