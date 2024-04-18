# 案例一：
# 1.输入用户年龄
age = int(input('请输入你的年龄：'))
# 2.判断是否满18岁
if age > 18:
    # 3.如果满18岁,允许进入网吧嗨皮
    print("你可以嗨皮了")
# 4.如果未满18岁,提示回家写作业
else:
    print("赶紧回家写作业去！")
# 案例二：
# 1.定义两个整数变量python_score/c_score，使用input获取成绩 编写代码判断成绩
python_score = int(input("请输入你的python成绩："))
c_score = int(input("请输入你的c成绩："))
if python_score > 60 or c_score > 60:
    print("您的成绩合格！")
# 2.要求只有一科成绩高于60就输出成绩及格
else:
    print("请您再接再厉！")
# 案例三：
# 1. 获取用户输入的用户名
name = input("请输入您的用户名：")
# 2. 判断用户名是 admin 时，在控制台输出：欢迎admin登录
if name == 'admin' or name == 'test':
    # 灵活使用格式化输出
    print(f"欢迎{name}登录！")
# 3. 判断用户名时 test 时，在控制台输出：欢迎test登录
# 4. 如果是其他信息，在控制台输出：查无此人！
else:
    print("查无此人！")
