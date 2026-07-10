# 字典操作示例
# 演示 Python 字典的增删改查、遍历以及安全取值

# 1. 创建字典
student = {
    "姓名": "张三",
    "年龄": 20,
    "专业": "计算机科学"
}
print("初始字典:", student)

# 2. 增加/修改键值对
student["学号"] = "2024001"
print("增加学号后:", student)

student["年龄"] = 21
print("修改年龄后:", student)

# 3. 删除键值对
del student["专业"]
print("删除专业后:", student)

major = student.pop("学号", "未知")
print(f"pop 学号: {major}, 剩余字典: {student}")

# 4. 查询取值
print("\n查询姓名:", student["姓名"])

# 使用 get() 安全取值（键不存在时不会报错）
print("get('姓名'):", student.get("姓名"))
print("get('成绩', '无'):", student.get("成绩", "无"))  # 提供默认值

# 5. 遍历字典
student = {
    "姓名": "李四",
    "年龄": 22,
    "专业": "人工智能",
    "成绩": 92
}

print("\n--- 遍历 keys() ---")
for key in student.keys():
    print(f"  键: {key}")

print("\n--- 遍历 values() ---")
for value in student.values():
    print(f"  值: {value}")

print("\n--- 遍历 items() ---")
for key, value in student.items():
    print(f"  {key}: {value}")

# 6. 检查键是否存在
print("\n'年龄' 在字典中吗?", "年龄" in student)
print("'性别' 在字典中吗?", "性别" in student)

# 7. 合并字典
extra = {"城市": "北京", "爱好": "编程"}
student.update(extra)
print("\n合并字典后:", student)
