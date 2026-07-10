#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_return_values.py
本脚本展示函数的返回值：
- 返回单个值
- 返回多个值（元组解包）
- 没有 return 时返回 None
"""


# 1. 返回单个值
def square(x):
    """计算一个数的平方。"""
    return x * x


print("=== 返回单个值 ===")
result = square(5)
print(f"square(5) = {result}")
print(f"square(8) = {square(8)}")

print("-" * 30)


# 2. 返回多个值（实际上是返回一个元组，可以被解包）
def get_min_max(numbers):
    """
    返回列表中的最小值和最大值。
    返回两个值时，实际上返回的是一个元组 (min, max)。
    """
    return min(numbers), max(numbers)


print("=== 返回多个值（元组解包）===")
nums = [23, 1, 89, 5, 42]
minimum, maximum = get_min_max(nums)
print(f"列表：{nums}")
print(f"最小值：{minimum}，最大值：{maximum}")

# 也可以整体接收为一个元组
result = get_min_max(nums)
print(f"整体接收：{result}，类型：{type(result)}")

print("-" * 30)


# 3. 没有 return 时返回 None
def say_hello(name):
    """只是打印问候，没有 return。"""
    print(f"你好，{name}！")


print("=== 没有 return 时返回 None ===")
return_value = say_hello("小明")
print(f"say_hello('小明') 的返回值：{return_value}")
print(f"返回值类型：{type(return_value)}")

print("-" * 30)


# 4. 显式返回 None
def check_positive(n):
    """如果是正数返回数值本身，否则返回 None。"""
    if n > 0:
        return n
    # 这里隐式返回 None


print("=== 条件性返回 None ===")
val1 = check_positive(10)
val2 = check_positive(-5)
print(f"check_positive(10)  = {val1}")
print(f"check_positive(-5)  = {val2}")
print(f"val2 is None        = {val2 is None}")

print("-" * 30)


# 5. 返回布尔值（常用于判断函数）
def is_even(n):
    """判断一个数是否为偶数。"""
    return n % 2 == 0


print("=== 返回布尔值 ===")
print(f"is_even(4) = {is_even(4)}")
print(f"is_even(7) = {is_even(7)}")
