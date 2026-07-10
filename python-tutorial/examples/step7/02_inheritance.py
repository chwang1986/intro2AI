# 继承示例
# 演示父类、子类继承、方法重写以及 super() 调用父类方法

class Animal:
    """动物父类"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """发出声音（子类应重写此方法）"""
        print(f"{self.name} 发出某种声音")

    def introduce(self):
        """介绍自己"""
        print(f"我是一只动物，叫 {self.name}")


class Dog(Animal):
    """狗类，继承自 Animal"""

    def __init__(self, name, breed):
        # 调用父类的构造方法
        super().__init__(name)
        self.breed = breed  # 狗品种

    def speak(self):
        """重写父类的 speak 方法"""
        print(f"{self.name} 说：汪汪！")

    def introduce(self):
        """重写并扩展父类方法"""
        super().introduce()  # 先调用父类的 introduce
        print(f"我是一只 {self.breed} 犬")


class Cat(Animal):
    """猫类，继承自 Animal"""

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        """重写父类的 speak 方法"""
        print(f"{self.name} 说：喵喵~")

    def introduce(self):
        """重写 introduce"""
        print(f"我是一只 {self.color} 色的猫，叫 {self.name}")


# 创建实例
dog = Dog("旺财", "金毛")
cat = Cat("咪咪", "白")

print("=== Dog 实例 ===")
dog.introduce()
dog.speak()

print("\n=== Cat 实例 ===")
cat.introduce()
cat.speak()

print("\n=== 多态演示：统一调用 speak ===")
animals = [Dog("大黄", "柴犬"), Cat("花花", "黑"), Animal("未知动物")]
for animal in animals:
    animal.speak()

print("\n=== 类型检查 ===")
print(f"dog 是 Animal 吗? {isinstance(dog, Animal)}")
print(f"dog 是 Dog 吗? {isinstance(dog, Dog)}")
print(f"dog 是 Cat 吗? {isinstance(dog, Cat)}")
