#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_hello.py
本脚本展示 print() 函数的基本用法：
- 打印 Hello World
- 打印多行文本
- 打印数字
- 使用 sep 和 end 参数
"""

# 1. 打印 Hello World
print("你好，世界！")

# 2. 打印多行文本（使用三引号）
print("""
这是第一行
这是第二行
这是第三行
""")

# 3. 打印数字
print(42)
print(3.14159)

# 4. print 的 sep 参数（分隔符，默认是空格）
print("苹果", "香蕉", "橙子")
print("苹果", "香蕉", "橙子", sep="、")
print("苹果", "香蕉", "橙子", sep="-")

# 5. print 的 end 参数（结尾，默认是换行符 \n）
print("这句话不会换行", end="")
print("，而是连在了一起")
print("自定义结尾", end="~~~")
print("下一行")
