# 异常处理示例
# 演示 try/except/finally 的用法，捕获多种异常类型

# 1. 捕获 ZeroDivisionError
print("=== 1. 捕获 ZeroDivisionError ===")
try:
    result = 10 / 0
    print("这行不会执行")
except ZeroDivisionError as e:
    print(f"捕获到除零错误: {e}")

# 2. 捕获 ValueError
print("\n=== 2. 捕获 ValueError ===")
try:
    number = int("abc")
except ValueError as e:
    print(f"捕获到数值错误: {e}")

# 3. 使用 finally 清理资源
print("\n=== 3. finally 总是执行 ===")
try:
    print("尝试打开不存在的文件...")
    f = open("不存在文件.txt", "r")
except FileNotFoundError as e:
    print(f"文件未找到: {e}")
finally:
    print("finally 块：无论是否异常，这里的代码都会执行")

# 4. 捕获多种异常类型
print("\n=== 4. 捕获多种异常类型 ===")
for value in [10, 0, "abc"]:
    try:
        if value == 0:
            result = 10 / value
        else:
            result = 10 / int(value)
            print(f"10 / {value} = {result}")
    except ZeroDivisionError:
        print(f"处理 {value}: 不能除以零!")
    except ValueError:
        print(f"处理 {value}: 无法转换为数字!")
    except Exception as e:
        print(f"处理 {value}: 其他错误: {e}")

# 5. else 子句（没有异常时执行）
print("\n=== 5. else 子句 ===")
try:
    result = 10 / 2
except ZeroDivisionError:
    print("除零错误")
else:
    print(f"没有异常，结果是: {result}")

# 6. 主动抛出异常
print("\n=== 6. 主动抛出异常 ===")
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(f"捕获到主动抛出的异常: {e}")
