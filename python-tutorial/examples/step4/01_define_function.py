#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_define_function.py
本脚本展示函数的定义与调用：
- 定义问候函数
- 定义计算面积的函数
- 展示函数文档字符串 docstring
"""


# 1. 定义一个简单的问候函数
def greet(name):
    """向指定的人打招呼。"""
    print(f"你好，{name}！欢迎学习 Python。")


# 2. 定义计算矩形面积的函数
def rectangle_area(width, height):
    """
    计算矩形的面积。

    参数:
        width (float): 矩形的宽度
        height (float): 矩形的高度

    返回:
        float: 矩形的面积
    """
    return width * height


# 3. 定义计算圆形面积的函数
def circle_area(radius):
    """计算圆的面积（使用近似值 3.14）。"""
    return 3.14 * radius * radius


# 4. 调用函数
print("=== 调用 greet() ===")
greet("小明")
greet("小红")

print("-" * 30)

print("=== 调用 rectangle_area() ===")
w = 5
h = 3
area = rectangle_area(w, h)
print(f"矩形宽度：{w}，高度：{h}")
print(f"矩形面积：{area}")

print("-" * 30)

print("=== 调用 circle_area() ===")
r = 4
print(f"圆的半径：{r}")
print(f"圆的面积：{circle_area(r)}")

print("-" * 30)

# 5. 查看函数的文档字符串
print("=== 查看文档字符串 ===")
print(f"greet 的说明：{greet.__doc__}")
print(f"rectangle_area 的说明：{rectangle_area.__doc__}")

# 也可以使用 help() 查看完整信息
print("\n使用 help() 查看 rectangle_area：")
help(rectangle_area)
