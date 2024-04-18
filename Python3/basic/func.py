import datetime
import tools


# 定义函数的格式：先定义def 再调用,因为python是顺序执行
def worklog():
    # def下方的三对双引号为函数的文档注释，选中函数Ctrl+Q查看
    """worklog"""
    print('-' * 21 + str(datetime.date.today()) + '-' * 20)
    logs = input('请输入您想记录的内容：')
    print(logs)
    print('-' * 21 + str(datetime.date.today()) + '-' * 20)


def sum_p(a, b):
    # 传参
    """one plus one"""
    c = a + b
    print(f"{a} + {b} = {c}")


# 嵌套使用
def test01():
    print(1)
    print("test01")
    print(2)


def test02():
    print(3)
    test01()
    print(4)


# 返回值
def get_max(a, b):
    """函数遇到return后会结束函数的执行"""
    if a > b:
        return a
    else:
        return b


# 空两行才能调用
# worklog()
# sum_p(10, 22)
# print(5)
# test02()
# print(6)
# num = get_max(20, 30)
# print(num)
t = tools.sum_2_num(10, 20)
print(t)
