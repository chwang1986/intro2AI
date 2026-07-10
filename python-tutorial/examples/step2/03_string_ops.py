#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_string_ops.py
本脚本展示字符串的常见操作：
- 切片、长度
- 大小写转换
- 查找、替换、拆分
"""

text = "Hello, Python 编程世界！"
print(f"原始字符串：{text}")
print(f"字符串长度：{len(text)}")
print("-" * 30)

# 1. 字符串切片
print("=== 切片 ===")
print(f"text[0]       = '{text[0]}'")           # 第一个字符
print(f"text[-1]      = '{text[-1]}'")          # 最后一个字符
print(f"text[0:5]     = '{text[0:5]}'")        # 前5个字符
print(f"text[7:13]    = '{text[7:13]}'")       # 第7到12个字符
print(f"text[:5]      = '{text[:5]}'")         # 从头到第5个
print(f"text[7:]      = '{text[7:]}'")         # 从第7个到末尾
print(f"text[::2]     = '{text[::2]}'")        # 每隔一个取一个
print(f"text[::-1]    = '{text[::-1]}'")       # 反转字符串

# 2. 大小写转换
print("\n=== 大小写转换 ===")
s = "Python Is Fun"
print(f"原字符串：       {s}")
print(f"upper()：        {s.upper()}")        # 全大写
print(f"lower()：        {s.lower()}")        # 全小写
print(f"capitalize()：   {s.capitalize()}")   # 首字母大写
print(f"title()：        {s.title()}")         # 每个单词首字母大写

# 3. 查找
print("\n=== 查找 ===")
t = "我喜欢 Python，Python 非常强大"
print(f"原字符串：{t}")
print(f"find('Python')   = {t.find('Python')}")     # 第一次出现的位置
print(f"rfind('Python')  = {t.rfind('Python')}")    # 最后一次出现的位置
print(f"count('Python')  = {t.count('Python')}")    # 出现次数
print(f"'Java' in t      = {'Java' in t}")          # 是否包含

# 4. 替换
print("\n=== 替换 ===")
new_t = t.replace("Python", "Java")
print(f"replace 后：{new_t}")
print(f"原字符串未变：{t}")  # 字符串是不可变的

# 5. 拆分
print("\n=== 拆分 ===")
fruits = "苹果,香蕉,橙子,葡萄"
print(f"原字符串：{fruits}")
fruit_list = fruits.split(",")
print(f"split(',') 结果：{fruit_list}")

sentence = "  Python   编程   很有趣  "
print(f"\n原字符串：'{sentence}'")
print(f"strip() 后：'{sentence.strip()}'")
print(f"split() 后：{sentence.split()}")  # 默认按空白拆分
