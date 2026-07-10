# 文件写入示例
# 演示写入文本、追加模式，以及读取验证

import os

demo_file = "temp_write_demo.txt"

# 1. 写入文本到文件（覆盖模式 'w'）
print("=== 步骤1：写入新文件 ===")
with open(demo_file, "w", encoding="utf-8") as f:
    f.write("这是第一行内容\n")
    f.write("这是第二行内容\n")
    f.write("写入数字: {}\n".format(42))
    print(f"已写入内容到 {demo_file}")

# 2. 追加模式写入（'a' = append）
print("\n=== 步骤2：追加内容 ===")
with open(demo_file, "a", encoding="utf-8") as f:
    f.write("--- 这是追加的内容 ---\n")
    f.write("追加一行：学习 Python 很有趣\n")
    print("已追加内容到文件末尾")

# 3. 读取验证内容
print("\n=== 步骤3：读取验证 ===")
with open(demo_file, "r", encoding="utf-8") as f:
    content = f.read()
    print("文件内容:")
    print(content)

# 4. 演示写入多行（writelines）
print("=== 步骤4：使用 writelines ===")
lines_to_write = [
    "使用 writelines 写入\n",
    "可以一次写入多行\n",
    "每一行都要自己加换行符\n"
]
with open(demo_file, "w", encoding="utf-8") as f:
    f.writelines(lines_to_write)

with open(demo_file, "r", encoding="utf-8") as f:
    print("写入后文件内容:")
    print(f.read())

# 清理
os.remove(demo_file)
print(f"已删除临时文件: {demo_file}")
