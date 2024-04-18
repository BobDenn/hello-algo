class Person:
    def __init__(self, name, age):
        self.name = name  # 公有属性
        self.__age = age  # 公有属性 -> 私有属性 __age

    def __str__(self):
        return f"{self.name}{self.__age}了"

    def set_age(self, age):
        if age < 0 or age > 100:
            print("请重新输入年龄")
            return
        self.__age = age


if __name__ == '__main__':
    dk = Person('邓阔', 18)
    print(dk)
    # 要想修改私有属性，可以创建一个专门的方法，例如set_age
    dk.age = 22
    # 外部方法不能改变私有属性
    print(dk)
    dk.set_age(22)
    print(dk)  # 修改成功
