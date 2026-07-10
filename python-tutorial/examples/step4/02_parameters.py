#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02_parameters.py
本脚本展示函数的参数用法：
- 位置参数
- 默认参数
- 关键字参数
- *args 接收任意多个参数
"""


# 1. 位置参数：按顺序传递
def introduce(name, age, city):
    """介绍一个人的基本信息。"""
    print(f"我叫{name}，今年{age}岁，来自{city}。")


print("=== 位置参数 ===")
introduce("小明", 20, "北京")
introduce("小红", 22, "上海")

print("-" * 30)


# 2. 默认参数：定义时给参数指定默认值
def make_coffee(coffee_type="美式", size="中杯"):
    """制作一杯咖啡。"""
    print(f"制作一杯 {size} 的 {coffee_type} 咖啡")


print("=== 默认参数 ===")
make_coffee()                     # 使用所有默认值
make_coffee("拿铁")               # 只覆盖第一个参数
make_coffee("卡布奇诺", "大杯")    # 覆盖所有参数
make_coffee(size="小杯")          # 用关键字只覆盖 size

print("-" * 30)


# 3. 关键字参数：调用时指定参数名
def book_flight(origin, destination, date, cabin="经济舱"):
    """预订航班。"""
    print(f"预订 {date} 从 {origin} 到 {destination} 的 {cabin} 机票")


print("=== 关键字参数 ===")
book_flight(origin="广州", destination="成都", date="2024-08-01")
book_flight(destination="东京", origin="北京", date="2024-09-10", cabin="商务舱")

print("-" * 30)


# 4. *args：接收任意多个位置参数
def sum_all(*numbers):
    """
    计算任意多个数字的总和。
    numbers 在函数内部是一个元组。
    """
    total = 0
    for n in numbers:
        total += n
    return total


print("=== *args 用法 ===")
print(f"sum_all()           = {sum_all()}")
print(f"sum_all(1, 2)       = {sum_all(1, 2)}")
print(f"sum_all(1, 2, 3, 4) = {sum_all(1, 2, 3, 4)}")

# 也可以传入列表/元组，用 * 解包
nums = [10, 20, 30]
print(f"sum_all(*nums)      = {sum_all(*nums)}")
