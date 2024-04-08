# list 列表的定义：空列表
# 列表中的值可以是多种数据类型
first_list = []  # 也可以写first_list = ()
# 创建一个新列表
num_list = [1, 2, 3, 4, 5]
#           0  1  2  3  4
print('新列表：', num_list)
# 列表支持下标和切片
print('第一个元素为：', num_list[0])  # 1
print('切片：', num_list[1:4:1])  # [2, 3, 4]  [起始位:结束位后一位:步长]
# index()查找方法，返回值是其索引
num = num_list.index(4)
print('查找下标为4的元素；', num)  # 3
# count()方法，可以返回列表中元素的个数
Num = num_list.count(2)
print('列表中有几个2：', Num)  # 1
# 列表添加.append()和删除.pop()方法
num_list.append('hello')
# 在列表尾部添加，返回None，因为他是直接在原列表中添加
num_list.append(2)
print('添加元素后的列表：', num_list)
# list.pop(index) 删除
num_list.pop(5)
print('删除元素后的列表：', num_list)
# 修改列表中的数据 list[index] = new data
num_list.append(7)  # [1, 2, 3, 4, 5, 2, 7]
num_list[5] = 6  # [1, 2, 3, 4, 5, 6, 7]
print('修改下标为5的数据之后的列表：', num_list)
# 列表反转 -- 两种方式： list[::-1] 或者使用.reverse()方法
# list[::-1]会产生新的列表，而reverse是修改原列表
new_list = num_list[::-1]
print('切片反转后的列表：', new_list)
num_list.reverse()
print('reverse方法反转的列表：', num_list)
# 列表的排序，要求数据类型一样，且是在原列表中排序
mynum = [8, 88, 234, 99, 1, 2, 3, 7]
mynum.sort()
print('升序：', mynum)
mynum.sort(reverse=True)
print('降序：', mynum)
# 列表可以嵌套
person = [['邓阔', '男', '自动化测试'], ['韩新宇', '女', '国际贸易']]
# 打印 男
print(person[0][1])
# 第二个列表增加 '美丽'
person[1].append('美丽')
print(person)
# 删除也是同理
# 查看列表中的元素个数
print(len(person))
