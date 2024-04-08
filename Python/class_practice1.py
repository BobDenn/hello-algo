class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print(f"{self.name}跑步了,体重减少了0.5公斤")

    def eat(self):
        self.weight += 1
        print(f"{self.name}大餐了,体重增加了1公斤")

    def __str__(self):
        return f"{self.name}目前的体重为{self.weight}公斤"


if __name__ == '__main__':
    jack = Person('jack', 64)
    jack.run()
    jack.eat()
    print(jack)
    jack.eat()
    jack.eat()
    print(jack)
