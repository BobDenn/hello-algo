class Dog:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"小狗{self.name}在跑步")

    def __str__(self):
        return f"我是：{self.name}"


dog = Dog("杰瑞")
dog.run()
# 对象中的 __str__ 方法是外部print(对象)打印出来的信息
# 如果没有定义__str__方法
print(dog)
