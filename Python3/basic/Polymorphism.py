class Dog:
    def game(self):
        print("普通狗只是简单的玩耍")


class XTQ(Dog):
    def game(self):
        print("哮天犬在天上玩耍")


class Person:
    def play_with_dog(self, dog):
        """dog是狗类或者其子类的对象"""
        print("人和狗在玩耍...")
        dog.game()


if __name__ == '__main__':
    dog1 = Dog()
    xtq = XTQ()
    wo = Person()
    wo.play_with_dog(dog1)
    wo.play_with_dog(xtq)
#  就是先用本对象的方法  然后传参其他对象 再用其他对象的方法
