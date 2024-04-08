name = '邓阔'
age = 24
gender = '男'
# 使用.format,依次填入变量
print("我是{}。我今年{}岁了，我是{}人！".format(name, age, gender))
num1 = int(input("请输入一个数字："))
num2 = int(input("请再输入一个数字："))
num = num1 + num2
# f或F加引号，用{}占位，并填写要引用的变量
print(f"{num1} + {num2} = {num}")
# 还有一种字符串拼接的，太麻烦就不写了
# id 可以查看变量的引用
print(f"a: {age}, {id(age)}")
