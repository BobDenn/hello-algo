class Cat:  # 成功创建一个类且包含方法,init方法是对象在创建时就会自动调用
    # 初始化对象，给对象添加属性
    def __init__(self):
        print("我是__init__方法，我被调用了")  # 验证使用

    @staticmethod  # 静态方法对参数没有要求，没有使用到self的就是静态方法
    def eat():
        """吃东西"""
        print("小猫爱吃东西...")

    def drink(self):
        # self是调用这个方法的对象
        """喝水"""
        print(f"小猫{self}会喝水...")


# 需要实例化一个有变量接收的对象，然后调用方法
cat = Cat()
# 不建议在类外面添加属性
# cat.name = '汤姆'
# 变量.方法名()
# cat.eat()
# cat.drink()
