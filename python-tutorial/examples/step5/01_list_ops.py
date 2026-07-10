# 列表操作示例
# 演示 Python 列表的增删改查、排序、反转、切片和列表推导式

# 1. 创建列表
fruits = ["苹果", "香蕉", "橙子"]
print("初始列表:", fruits)

# 2. 增加元素
fruits.append("葡萄")
print("append 后:", fruits)

fruits.insert(1, "芒果")
print("insert(1, '芒果') 后:", fruits)

# 3. 删除元素
fruits.remove("香蕉")
print("remove('香蕉') 后:", fruits)

popped = fruits.pop()
print(f"pop() 移除末尾元素: {popped}, 列表变为: {fruits}")

# 4. 修改元素
fruits[0] = "西瓜"
print("修改 fruits[0] 为 '西瓜':", fruits)

# 5. 查找元素
print("'橙子' 在列表中吗?", "橙子" in fruits)
print("'橙子' 的索引:", fruits.index("橙子"))

# 6. 列表排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("\n原始数字列表:", numbers)
numbers.sort()
print("sort() 升序后:", numbers)
numbers.sort(reverse=True)
print("sort(reverse=True) 降序后:", numbers)

# 7. 列表反转
letters = ["a", "b", "c", "d"]
letters.reverse()
print("\n反转 letters:", letters)

# 8. 切片操作
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\n切片 nums[2:5]:", nums[2:5])      # 索引 2 到 4
print("切片 nums[:3]:", nums[:3])        # 开头到索引 2
print("切片 nums[7:]:", nums[7:])        # 索引 7 到末尾
print("切片 nums[::2]:", nums[::2])      # 每隔一个取一个
print("切片 nums[::-1]:", nums[::-1])    # 反转列表

# 9. 列表推导式
squares = [x**2 for x in range(5)]
print("\n列表推导式 [x**2 for x in range(5)]:", squares)

evens = [x*2 for x in range(10) if x % 2 == 0]
print("带条件的列表推导式:", evens)
