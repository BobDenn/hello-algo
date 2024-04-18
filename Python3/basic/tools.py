def sum_2_num(a, b):
    """求和函数"""
    return a + b


# 模块中__name__变量默认是__main__
# 导入模块时，模块中的代码会自动执行，且__name__变量会改变成模块名，
# 此时 __name__ != '__main__',所以代码不会运行
if __name__ == '__main__':
    print('这是我的__name__变量: ', __name__)
    print(sum_2_num(2, 3))
# 此处的作用是此文件内可运行，被别的文件导入时不运行
