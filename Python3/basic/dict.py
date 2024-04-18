# 字典定义 -- 键值对
my_dict = {'姓名': '韩', '年龄': '22', '身高': '155', '性别': '女'}
print('初始字典：', my_dict)
# 增改 -- 字典[键] = 值，存在就是修改，不存在就是新建
my_dict['年龄'] = 21
my_dict['对象'] = '邓阔'
print("增加修改后：", my_dict)
# 删除 -- my_dict.pop(键)
my_dict.pop('年龄')
print('删除后：', my_dict)
# 查询 -- 方法1：字典[键] 不存在的话会报错不建议
# print(my_dict['qwe'])
# 查询 -- 方法1：my_dict.get(键)  返回None
print('查询：', my_dict.get('name'))
# 遍历 键、值、键值
for k in my_dict.keys():
    print(k)
print('*' * 30)
for v in my_dict.values():
    print(v)
print('*' * 30)
for k, v in my_dict.items():
    print(k, v)
print('*' * 30)
# in 操作符 判断容器中是否存在这个键
print('年龄' in my_dict)
# 看一看字典的长度是什么 -- 一对是一个元素
print(len(my_dict))
