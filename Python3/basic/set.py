# 集合 {}  集合中不能有重复的数据，主要是对列表进行 去重操作
list1 = [1, 2, 2, 3, 4, 5, 2, 3, 4]
print(list(set(list1)))
new_list = []
# 遍历源列表
for i in list1:
    # 判断是否存在于新列表
    if i not in new_list:
        # 存在则跳过
        # pass
        # else:
        # 不存在则添加
        new_list.append(i)
print(new_list)
