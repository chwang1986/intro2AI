# 集合与元组示例
# 演示 Python 集合的去重、集合运算，以及元组的创建和解包

# ==================== 集合 (set) ====================
print("=== 集合操作 ===")

# 1. 创建集合
fruits = {"苹果", "香蕉", "橙子", "苹果"}  # 重复元素会被自动去重
print("创建集合 (自动去重):", fruits)

# 从列表创建集合（去重）
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_nums = set(numbers)
print(f"列表 {numbers} 去重后:", unique_nums)

# 2. 添加和删除元素
fruits.add("葡萄")
print("add('葡萄') 后:", fruits)
fruits.discard("香蕉")
print("discard('香蕉') 后:", fruits)

# 3. 集合运算
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("\n集合 A:", set_a)
print("集合 B:", set_b)

print("交集 (A & B):", set_a & set_b)
print("并集 (A | B):", set_a | set_b)
print("差集 (A - B):", set_a - set_b)
print("对称差集 (A ^ B):", set_a ^ set_b)  # 仅在其中一个集合中的元素

# 也可以用方法调用
print("\n方法调用:")
print("A.intersection(B):", set_a.intersection(set_b))
print("A.union(B):", set_a.union(set_b))
print("A.difference(B):", set_a.difference(set_b))

# ==================== 元组 (tuple) ====================
print("\n=== 元组操作 ===")

# 1. 创建元组（不可变序列）
coords = (10, 20)
print("坐标元组:", coords)

rgb = (255, 128, 0)
print("颜色 RGB 元组:", rgb)

# 单元素元组需要逗号
single = (42,)
print(f"单元素元组: {single}, 类型: {type(single)}")

# 2. 元组解包
x, y = coords
print(f"\n解包坐标: x={x}, y={y}")

r, g, b = rgb
print(f"解包颜色: r={r}, g={g}, b={b}")

# 3. 元组作为字典的 key（因为元组不可变，可哈希）
locations = {
    (0, 0): "原点",
    (10, 20): "商店",
    (30, 40): "学校"
}
print("\n以元组为键的字典:")
for point, name in locations.items():
    print(f"  位置 {point} -> {name}")

print("\n查询位置 (10, 20):", locations.get((10, 20), "未知地点"))
