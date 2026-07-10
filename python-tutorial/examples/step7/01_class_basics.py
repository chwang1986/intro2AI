# 类的基本概念示例
# 演示如何定义类、__init__ 构造方法、属性和方法

class Dog:
    """狗类，表示一只宠物狗"""

    def __init__(self, name, age):
        """构造方法：创建实例时自动调用"""
        self.name = name  # 实例属性：名字
        self.age = age    # 实例属性：年龄

    def bark(self):
        """狗叫方法"""
        print(f"{self.name} 说：汪汪！")

    def introduce(self):
        """自我介绍"""
        print(f"大家好，我是 {self.name}，今年 {self.age} 岁。")

    def have_birthday(self):
        """过生日，年龄加1"""
        self.age += 1
        print(f"{self.name} 过生日了，现在 {self.age} 岁！")


# 创建多个 Dog 实例
dog1 = Dog("旺财", 3)
dog2 = Dog("来福", 2)
dog3 = Dog("豆豆", 1)

print("=== 狗狗自我介绍 ===")
dog1.introduce()
dog2.introduce()
dog3.introduce()

print("\n=== 狗狗叫 ===")
dog1.bark()
dog2.bark()
dog3.bark()

print("\n=== 过生日 ===")
dog3.have_birthday()

print("\n=== 访问属性 ===")
print(f"{dog1.name} 的年龄是 {dog1.age}")
print(f"{dog2.name} 的年龄是 {dog2.age}")
