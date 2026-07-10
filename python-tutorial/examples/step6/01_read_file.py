# 文件读取示例
# 演示使用 with open() 读取文件的不同方式
# 脚本自行创建临时文件，不依赖外部文件

import os

# 先创建一个临时文件供读取
temp_file = "temp_read_demo.txt"

# 写入演示内容
with open(temp_file, "w", encoding="utf-8") as f:
    f.write("第一行：Python 文件操作很简单\n")
    f.write("第二行：with 语句可以自动关闭文件\n")
    f.write("第三行：记得指定 encoding='utf-8'\n")
    f.write("第四行：逐行读取是常见做法\n")

print(f"已创建临时文件: {temp_file}\n")

# 1. 使用 with open() 读取整个文件内容
print("=== 方式1：读取全部内容 ===")
with open(temp_file, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 2. 逐行读取（常用）
print("=== 方式2：逐行读取 ===")
with open(temp_file, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        print(f"  第 {line_num} 行: {line.strip()}")

# 3. 读取所有行到列表
print("\n=== 方式3：读取所有行到列表 ===")
with open(temp_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("行列表:", lines)
    print("共", len(lines), "行")

# 4. 逐行读取并处理
print("\n=== 方式4：读取并过滤包含特定文字的行 ===")
with open(temp_file, "r", encoding="utf-8") as f:
    for line in f:
        if "with" in line or "Python" in line:
            print(f"  -> {line.strip()}")

# 清理临时文件
os.remove(temp_file)
print(f"\n已删除临时文件: {temp_file}")
